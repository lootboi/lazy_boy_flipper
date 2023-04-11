from utils import red, blue, yellow, white, green
from utils import headers
from utils import encode_attributes
from utils import get_avax_price
from utils import get_collection_overview

import json
import asyncio
import aiohttp

from aiolimiter import AsyncLimiter
from aiohttp.connector import TCPConnector
from aiohttp import ClientTimeout

# limit to 450 requests per second
limiter = AsyncLimiter(450, 1)
connector = TCPConnector(limit=450)


async def single_request(url, session, semaphore, max_retries=3):

    await semaphore.acquire()
    retry_delay = 1
    for attempt in range(1, max_retries + 1):
        try:
            async with limiter:  # Set the desired timeout in seconds
                async with session.get(url, headers=headers) as resp:
                    content = await resp.read()
                    semaphore.release()
                    return content
        except Exception as e:
            print(f"Error during request: {e}. Attempt {attempt}/{max_retries}. Retrying in {retry_delay} seconds...")
            if attempt < max_retries:
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Increase the retry delay for the next attempt
            else:
                print(f"Max retries reached for URL: {url}. Skipping this request.")
                semaphore.release()
                return None

        
def generate_url(collection_address, encoded_filter):
    url = f"https://api.joepegs.dev/v3/items?filters=buy_now&orderBy=price_asc&collectionAddress={collection_address}&attributeFilters={encoded_filter}&limit=1"
    return url

async def batch_attribute_request(semaphore, encoded_filters_array, collection_address):
    timeout = ClientTimeout(total=30)  # Set the desired timeout in seconds
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [
            single_request(
                generate_url(collection_address, encoded_filter),
                session,
                semaphore,
            )
            for encoded_filter in encoded_filters_array
        ]
        results = await asyncio.gather(*tasks)
        return results

async def retry_requests(retry_attributes, avax_price):
    attribute_results = []

    # Get the price of AVAX
    avax_price = await get_avax_price()

    async with aiohttp.ClientSession() as session:
        for retry_item in retry_attributes:
            if retry_item['trait_type_count'] == 0:
                print(f"Skipping {retry_item['trait_type']} since attributeCount is 0.")
                attribute_results.append({
                    'attribute': retry_item['trait_type'],
                    'attributeType': retry_item['traits'],
                    'attributeCount': retry_item['trait_type_count'],
                    'attributePercent': float(retry_item['trait_percentage']),
                    'floor': None,
                    'usdFloor': None
                })
                continue
            
            success = False
            attempts = 0
            while not success and attempts < 3:
                attempts += 1
                result = await single_request(retry_item['url'], session, asyncio.Semaphore(450))
                if result is not None:
                    try:
                        data = json.loads(result)
                        if isinstance(data, list) and len(data) > 0 and 'currentAsk' in data[0]:
                            current_price = int(data[0]['currentAsk']['price'])
                            current_price_ether = round(current_price * 1e-18, 4)
                            usd_price = current_price_ether * avax_price
                            ether_formatted = float(current_price_ether)
                            attribute_results.append({
                                'attribute': retry_item['trait_type'],
                                'attributeType': retry_item['traits'],
                                'attributeCount': retry_item['trait_type_count'],
                                'attributePercent': float(retry_item['trait_percentage']),
                                'floor': ether_formatted,
                                'usdFloor': round(usd_price, 2)
                            })
                            success = True
                        else:
                            print(red + f"Error: Invalid response for {retry_item['trait_type']} (attempt {attempts}/3). Retrying..." + white)
                            await asyncio.sleep(2)
                    except json.JSONDecodeError:
                        print(yellow + f"Error: Invalid JSON response for {retry_item['trait_type']} (attempt {attempts}/3). Retrying..." + white)
                        await asyncio.sleep(2)
                else:
                    print(blue + f"Result is None for {retry_item['trait_type']} (attempt {attempts}/3). Retrying...")
                    await asyncio.sleep(2)
    return attribute_results



async def query_single_attribute(attribute, collection_address, avax_price):

    attribute_results = []  # Initialize the list to store the attribute results
    retry_attributes = []  # Initialize the list to store the attributes that need to be retried

    traits = attribute['traitType']
    types_array = []
    value_count = []

    # Get the price of AVAX
    avax_price = await get_avax_price()

    # Calculate total sum of trait_type_count for this attribute
    total_sum = sum([trait['count'] for trait in attribute['values']])

    encoded_filters = []
    for trait in attribute['values']:
        trait_type = trait['value']
        trait_type_count = trait['count']
        trait_percentage = str("%.2f" % ((trait_type_count / total_sum) * 100))
        types_array.append(trait_type)
        value_count.append(trait_type_count)
        encoded_filters.append(encode_attributes(traits, trait_type))

    semaphore = asyncio.Semaphore(450)
    results = await batch_attribute_request(semaphore, encoded_filters, collection_address)

    for result, trait_type, encoded_filter in zip(results, types_array, encoded_filters):
        if result is not None:
            try:
                data = json.loads(result)
                if isinstance(data, list) and len(data) > 0 and 'currentAsk' in data[0]:
                    current_price = int(data[0]['currentAsk']['price'])
                    current_price_ether = round(current_price * 1e-18, 4)
                    usd_price = current_price_ether * avax_price
                    ether_formatted = float(current_price_ether)
                    attribute_results.append({
                        'attribute': trait_type,
                        'attributeType': traits,
                        'attributeCount': trait_type_count,
                        'attributePercent': float(trait_percentage),
                        'floor': ether_formatted,
                        'usdFloor': usd_price
                    })
                else:
                    print(red + f"Invalid response for {trait_type}. Adding to retry list." + white)
                    retry_attributes.append({
                        'trait_type': trait_type,
                        'traits': traits,
                        'trait_type_count': trait_type_count,
                        'trait_percentage': trait_percentage,
                        'url': generate_url(collection_address, encoded_filter)
                    })
            except json.JSONDecodeError:
                print(red + f"Error: Invalid JSON response for {trait_type}. Adding to retry list." + white)
                retry_attributes.append({
                    'trait_type': trait_type,
                    'traits': traits,
                    'trait_type_count': trait_type_count,
                    'trait_percentage': trait_percentage,
                    'url': generate_url(collection_address, encoded_filter)
                })

    # Retry requests for attributes with invalid responses
    if retry_attributes:
        print(yellow + "Retrying requests for attributes with invalid responses..." + white)
        retry_results = await retry_requests(retry_attributes, avax_price)
        attribute_results.extend(retry_results)

    print('All queries not requiring retries have been completed.')

    return attribute_results



async def main():
    print(white)
    collection_address = "0xb5d5b4cd4303d985d83c228644b9ed10930a8152"
    attributes = get_collection_overview(collection_address)

    avax_price = await get_avax_price()  # Fetch AVAX price once

    all_valid = False
    while not all_valid:
        all_valid = True
        for attribute in attributes['attributes']: #
            attribute_results = await query_single_attribute(attribute, collection_address, avax_price)  # Remove asyncio.run() and directly use await
            for result in attribute_results:
                if result['floor'] is None or result['usdFloor'] is None:
                    all_valid = False

    print(green + "All attributes have valid floor prices!" + white)

if __name__ == "__main__":
    asyncio.run(main())

