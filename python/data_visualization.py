from colors import yellow, white, blue
from utils import headers
from utils import encode_attributes
from utils import get_avax_price

import json
import asyncio
import aiohttp
import plotext as plt

from aiolimiter import AsyncLimiter
from aiohttp.connector import TCPConnector
from aiohttp import ClientTimeout

# limit to 500 requests per second
limiter = AsyncLimiter(500, 1)
connector = TCPConnector(limit=500)


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

async def visualize_attributes(attributes, collection_address):

    avax_price = await get_avax_price()

    trait_type_array = []
    for attribute in attributes['attributes']:
        traits = attribute['traitType']
        trait_type_array.append(traits)
        types_array = []
        value_count = []
        
        # Calculate total sum of trait_type_count for this attribute
        total_sum = sum([trait['count'] for trait in attribute['values']])
        
        encoded_filters = []
        for trait in attribute['values']:
            trait_type = trait['value']
            trait_type_count = trait['count']
            trait_percentage = str( "%.2f" % ((trait_type_count / total_sum) * 100)) 
            types_array.append(trait_type + ' (' + trait_percentage + '%)')
            value_count.append(trait_type_count)
            encoded_filters.append(encode_attributes(traits, trait_type))

        semaphore = asyncio.Semaphore(500)
        results = await batch_attribute_request(semaphore, encoded_filters, collection_address)
        
        for result, trait_type in zip(results, types_array):
            if result is not None:
                try:
                    data = json.loads(result)
                    # Check if data is a list and has at least one item, and if 'currentAsk' exists in the first item
                    if isinstance(data, list) and len(data) > 0 and 'currentAsk' in data[0]:
                        current_price = int(data[0]['currentAsk']['price'])
                        current_price_ether = round(current_price * 1e-18, 4)
                        usdFormatted = f"${current_price_ether * avax_price:,.2f}"
                        ether_formatted = f"{current_price_ether:,.2f}"
                        print( blue + trait_type + " : " + yellow + ether_formatted + white + " AVAX, USD price: " + yellow + usdFormatted + white) 
                    else:
                        print("No 'currentAsk' available for", trait_type)
                except json.JSONDecodeError:
                    print(f"Error: Invalid JSON response for trait type {trait_type}")

        plt.simple_bar(types_array, value_count, width=100, title=yellow + 'Distribution of ' + traits + ' types' + white)
        plt.show()

        # Find the rarest and least rare traits
        non_zero_value_count = [count for count in value_count if count > 0]
        rarest_index = value_count.index(min(non_zero_value_count))
        least_rare_index = value_count.index(max(non_zero_value_count))
        
        print("Rarest trait: ", types_array[rarest_index])
        print("Least rare trait: ", types_array[least_rare_index])
        print('\n')
        await asyncio.sleep(5)
