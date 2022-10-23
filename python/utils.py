from menu       import get_collection_info, collections_info_options, get_collection_item
from colors     import pblue, pred, white, yellow, red
from dotenv     import load_dotenv
from web3       import Web3

import os
import requests

# Load .env file
load_dotenv()

# Get API key from .env file
key = os.getenv('API_KEY')

# Create Authentification header
headers = {'x-joepegs-api-key': key}

# Get RPC URL from .env file
rpc_url = os.getenv('RPC_URL')

# Create web3 instance
w3 = Web3(Web3.HTTPProvider(rpc_url))

def convert_ether(wei):
    return w3.fromWei(int(wei), 'ether')

def get_avax_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=avalanche-2&vs_currencies=usd').json()
    avax_price = response['avalanche-2']['usd']
    return avax_price

def query_collection_info(collection_response):
    pblue('Querying Collection Info...')
    print()
    # Basic Collection Info
    collection_info = requests.get('https://api.joepegs.dev/v2/collections/' + collection_response + '/?filterBy=1d', headers=headers).json()
    collection_name = collection_info['name']
    collection_description = collection_info['description']

    # Collection Volume Info
    collection_floor = convert_ether(collection_info['floor'])
    collection_total_volume = convert_ether(collection_info['volumeTotal'])
    collection_volume_delta = collection_info['pctVolumeChanged']
    collection_floor_delta = collection_info['pctFloorPriceChanged']

    # Collection Marketplace Info
    collection_num_listed = collection_info['numAsks']
    collection_num_owners = collection_info['numOwners']
    collection_num_sales = collection_info['numSales']

    # USD Price Info
    avax_price = get_avax_price()
    collection_floor_usd = float(collection_floor) * avax_price
    collection_total_volume_usd = float(collection_total_volume) * avax_price

    pblue('Collection Name: ' + white + str(collection_name))
    pblue('Collection Description: ' + white + str(collection_description))
    pblue('Collection Holders: ' + white + str(collection_num_owners))
    print()
    pblue('Collection Total Sales: ' + white + str(collection_num_sales))
    pblue('Collection Listings: ' + white + str(collection_num_listed))
    pblue('Collection Floor: ' + white + '%.2f' % collection_floor + ' AVAX ' + yellow + '($' + str('%.2f' % collection_floor_usd) + ')')
    pblue('Collection Total Volume: ' + white + '%.2f' % collection_total_volume + ' AVAX ' + yellow + '($' + str('%.2f' % collection_total_volume_usd) + ')')
    pblue('Collection Volume 24H Change: ' + white + str(collection_volume_delta) + '%')
    pblue('Collection Floor 24H Change: ' + white + str(collection_floor_delta) + '%')
    print()
    pblue('Collection Marketplace Link: ' + white + 'https://joepegs.com/collections/' + convert_url(collection_name))

def collection_info():
    menu_response = collections_info_options()
    if menu_response == '1':
        print()
        pblue('View Collection Info')
        collection_response = get_collection_info()
        if w3.isAddress(collection_response):
            print()
            query_collection_info(collection_response)
        else:
            pred('Invalid Address - Try Again')
            get_collection_info()
    if menu_response == '2':
        print('Search for Collection Item')
        collection_address = get_collection_info()
        item_id = get_collection_item()
        get_item_info(collection_address, item_id)
    if menu_response == '3':
        print('Exiting...')
        exit()

def convert_url(collection_name):
    collection_name = collection_name.replace(' ', '-')
    collection_name = collection_name.lower()
    return collection_name

def get_collection_website(collectionId):
    collection = requests.get('https://api.joepegs.dev/v2/collections/' + collectionId, headers=headers).json()
    collection_website = collection['websiteUrl']
    return collection_website

def trending_collections():
    print()
    pblue('Finding Trending Collections...')
    print()
    trending_collections = requests.get('https://api.joepegs.dev/v2/collections/trending/', headers=headers).json()
    for collection in trending_collections:
        pblue(collection['collectionName'] + ' - ' + yellow +  collection['collectionId'])
        pblue('Collection MarketPlace Link: ' + white + 'https://joepegs.com/collections/' + convert_url(collection['collectionName']))
        website = get_collection_website(collection['collectionId'])
        pblue('Collection Website: ' + white + str(website))
        pblue('# of Items: ' + white + str(collection['numItems']))
        pblue('Floor: ' + white + str(convert_ether(int(collection['floorPrice']))) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(convert_ether(int(collection['floorPrice']))) * get_avax_price())) + ')')
        print()
    pblue('Would you like to do something else?')

def parse_attributes(item_attributes):
    pblue('Item Attributes:')
    for i  in  range(len(item_attributes)):
        pblue(item_attributes[i]['traitType'] + ': ' + white + item_attributes[i]['value'] + yellow + ' (Rarity: ' + str(float(item_attributes[i]['countPercentage']) * float(100)) + '%)')
    print()

def get_collection_supply(_collection):
    item_info = requests.get('https://api.joepegs.dev/v2/collections/' + _collection)
    collection_supply = item_info['numItems']
    return collection_supply

def get_item_info(collection, id_number):
    print()
    pblue('Finding Item Info...')
    print()
    item_info = requests.get('https://api.joepegs.dev/v2/collections/' + collection + '/tokens/' + id_number, headers=headers).json()
    item_name = item_info['collectionName']
    item_floor = convert_ether(item_info['floorPrice'])
    item_owner = item_info['owner']['ownerId']
    item_owner_total = item_info['owner']['quantity']
    item_attributes = item_info['metadata']['attributes']
    if item_info['rarityScore'] == 0.0:
        item_rarity =  red + 'No Rarity Score'
    else:
        item_rarity = item_info['rarityScore']
    
    if item_info['rarityRanking'] == None:
        item_ranking = red + 'No Rarity Ranking'
    else:
        item_ranking = item_info['rarityRanking']

    if item_info['currentAsk'] == None:
        item_current_ask = red + 'Not currently Listed for'
    else:
        item_current_ask = convert_ether((item_info['currentAsk']['price']))

    item_rarity_percentage = item_ranking / get_collection_supply(item_info['collection']) * 100

    pblue('Item Name: ' + white + item_name + ' #' + id_number)
    print()
    parse_attributes(item_attributes)
    pblue('Item Rarity: ' + white + str(item_rarity))
    pblue('Item Ranking: ' + white + str(item_ranking) + yellow + ' (' + str('%.2f' % item_rarity_percentage) + '%)')
    pblue('Item Floor: ' + white + str(item_floor) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(item_floor) * get_avax_price())) + ')')
    pblue('Item Current Ask: ' + white + str(item_current_ask) + ' AVAX')
    pblue('Item Owner: ' + white + str(item_owner) + yellow + ' (Owns ' + str(item_owner_total) + ' total)')

def sort_by_attribute(_collection, _item_id, _attribute):
    print()
    pblue('Sorting by ' + _attribute + '...')
    print()
    # item_info = requests.get('https://api.joepegs.dev/v2/items/' + _collection + '/tokens/' + _item_id, headers=headers).json()
    
def get_collection_by_attribute():
    print()
    pblue('Search by Attribute')
    _collection = get_collection_info()
    _item_id = get_collection_item()
    _attribute = get_collection_by_attribute()
    sort_by_attribute(_collection, _item_id, _attribute)    