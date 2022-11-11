from discord_util   import discord_alert
from transactions   import purchase_nft
from menu           import get_collection_address_user, collections_info_options, get_collection_item, get_attribute, get_attribute_value
from colors         import pblue, pred, white, yellow, red, pyellow, lgreen, green, blue
from dotenv         import load_dotenv
from web3           import Web3

import os
import time
import requests
import urllib.parse

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

#####################
#   Wei to Ether    #
#####################

def convert_ether(wei):
    return w3.fromWei(int(wei), 'ether')

#####################
#   Current Price   #
#####################

def get_avax_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=avalanche-2&vs_currencies=usd').json()
    avax_price = response['avalanche-2']['usd']
    return avax_price

########################################
#   Convert Collection Names for URL   #
########################################

def convert_url(collection_name):
    collection_name = collection_name.replace(' ', '-')
    collection_name = collection_name.lower()
    return collection_name

###################################
#   Retrieve Collection Website   #
###################################

def get_collection_website(collectionId):
    collection = requests.get('https://api.joepegs.dev/v2/collections/' + collectionId, headers=headers).json()
    collection_website = collection['websiteUrl']
    return collection_website

###################################
#   Retreive Top 10 Collections   #
###################################

def trending_collections():
    pblue('\nFinding Trending Collections...\n')
    trending_collections = requests.get('https://api.joepegs.dev/v2/collections/trending/', headers=headers).json()
    avax_price = get_avax_price()
    for collection in trending_collections:
        pblue(collection['collectionName'] + ' - ' + yellow +  collection['collectionId'])
        pblue('Collection MarketPlace Link: ' + white + 'https://joepegs.com/collections/' + convert_url(collection['collectionName']))
        website = get_collection_website(collection['collectionId'])
        pblue('Collection Website: ' + white + str(website))
        pblue('# of Items: ' + white + str(collection['numItems']))
        pblue('Floor: ' + white + str(convert_ether(int(collection['floorPrice']))) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(convert_ether(int(collection['floorPrice']))) * avax_price
        )) + ')\n')
    pblue('\nWould you like to do something else?')

def print_collection_overview(query_response):

    collection_name = query_response['name']
    collection_desc = query_response['description']
    collection_address = query_response['address']
    is_verified = query_response['verified']
    if is_verified == 'verified':
        is_verified = green + 'Verified'
    if is_verified != 'verified':
        is_verified = red + 'Not Verified [Could be fake]'

    num_items = str(query_response['numItems'])
    num_owners = str(query_response['numOwners'])

    total_volume = str("%.2f" % convert_ether(int(query_response['volume'])))
    total_sales = str(query_response['numSales'])
    floor = str("%.2f" % convert_ether(int(query_response['floor'])))
    total_listings = str(query_response['numAsks'])
    percent_listed = float((int(total_listings)/int(num_items))*100)
    
    avax_price = get_avax_price()
    average_avax_sale = float(total_volume)/float(total_sales)
    average_sale_usd = str('${:,.2f}'.format(avax_price*average_avax_sale))
    total_volume_usd = str('${:,.2f}'.format(avax_price*float(total_volume)))
    floor_usd = float(floor)*avax_price

    disc_url = query_response['discordUrl']
    if disc_url != None:
        disc_url = disc_url
    if disc_url == None:
        disc_url = red + 'No Discord link available'
    twitter_url = query_response['twitterUrl']
    if twitter_url != None:
        twitter_url = twitter_url
    if twitter_url == None:
        twitter_url = red + 'No Twitter link available'
    joepeg_url = 'https://joepegs.com/collections/' + collection_address

    pblue('\nCollection: ' + white + collection_name)
    pyellow('Collection Description: ' + white + collection_desc + '\n')
    pblue('Market Information:')
    pyellow('Items in Collection: ' + white + num_items)
    pyellow('Total Owners: ' + white + num_owners)
    pyellow('Total # of Sales: ' + white + total_sales)
    pyellow('Total Listings: ' + white + total_listings + green + ' (' + "%.2f" % percent_listed + '%' + ' listed)')
    pyellow('Total Volume: ' + white + total_volume + ' AVAX ' + green + '(' + total_volume_usd + ')')
    pyellow('Average Sale price: ' + white + "%.2f" % average_avax_sale + ' AVAX ' + green + '(' + average_sale_usd + ')')
    pyellow('Current Floor: ' + floor + ' AVAX ' + green + '($' + "%.2f" % floor_usd + ')\n')
    pblue('Collection Links:')
    pyellow('Joepeg Marketplace: ' + white + joepeg_url)
    pyellow('Twitter: ' + white + twitter_url)
    pyellow('Discord: ' + white + disc_url)

###################################
#   Parse Collection Attributes   #
###################################

def parse_collection_attributes(collection_attributes, collection_supply):
    pblue('\nCollection Attributes:')
    for attribute in collection_attributes:
        attribute_type = attribute['traitType']
        attribute_values = attribute['values']
        pblue('\nTrait type ' + attribute_type + ' has ' + yellow + str(len(attribute_values)) + blue + ' variations:\n')
        for value in attribute_values:
            attribute_value = value['value']
            value_distribution = value['count']
            distribution_percentage = float((value_distribution/collection_supply)*100)
            pyellow(attribute_value + green + ' [' + "%.2f" % distribution_percentage + '%]')

#############################
#   Parse Item Attributes   #
#############################

def parse_item_attributes(item_attributes):
    pblue('\nItem Attributes:')
    for i  in  range(len(item_attributes)):
        pblue(item_attributes[i]['traitType'] + ': ' + white + item_attributes[i]['value'] + yellow + ' Count: ' + str(item_attributes[i]['count']) + green + ' (Rarity: ' + "%.2f" % (float(item_attributes[i]['countPercentage'])*100) + '%)')

def get_item_overview(collection_address, id_number):
    item_overview = requests.get('https://api.joepegs.dev/v2/collections/' + collection_address + '/tokens/' + id_number, headers=headers).json()
    return item_overview

##############################
#   Get Specific Item Info   #
##############################

def get_item_info(collection, id_number):

    pblue('\nFinding Item Info...\n')
    
    item_info = get_item_overview(collection, id_number)
    item_name = item_info['collectionName']
    item_floor = convert_ether(item_info['floorPrice'])
    item_owner = item_info['owner']['ownerId']
    item_owner_total = item_info['owner']['quantity']
    item_attributes = item_info['metadata']['attributes']
    item_highest_bid = int(item_info['bestBid']['price'])
    avax_price = get_avax_price()

    if item_info['rarityScore'] == 0.0:
        item_rarity =  red + 'No Rarity Score'
    else:
        item_rarity = item_info['rarityScore']
    
    if item_info['rarityRanking'] == None:
        item_ranking = red + 'No Rarity Ranking'
    else:
        item_ranking = item_info['rarityRanking']

    item_collection = requests.get('https://api.joepegs.dev/v2/collections/' + collection, headers=headers).json()
    collection_supply = item_collection['numItems']

    if item_ranking == red + 'No Rarity Ranking':
        item_rarity_percentage = float(1) / float(collection_supply) * 100
    else:
        item_rarity_percentage = float(item_ranking) / float(collection_supply) * 100

    pblue('Item Name: ' + white + item_name + ' #' + id_number)
    parse_item_attributes(item_attributes)
    pblue('\nItem Rarity: ' + white + str(item_rarity) if item_rarity != red + 'No Rarity Ranking' else item_rarity_percentage + '%')
    pblue('Item Ranking: ' + white + str(item_ranking) + '/' + str(collection_supply) + yellow + ' (' + str('%.2f' % item_rarity_percentage) + '%)')
    pblue('Item Floor: ' + white + str(item_floor) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(item_floor) * avax_price)) + ')')
    if item_info['currentAsk'] == None:
        item_current_ask = red + 'Not currently Listed'
        pblue('Item Current Ask: ' + item_current_ask)
    else:
        item_current_ask = convert_ether((item_info['currentAsk']['price']))
        pblue('Item Current Ask: ' + white + str(item_current_ask) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(item_current_ask) * avax_price)) + ')')
    pblue('Item Highest Bid: ' + white + str(convert_ether(int(item_highest_bid))) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(convert_ether(int(item_highest_bid))) * avax_price)) + ')')
    pblue('Item Owner: ' + white + str(item_owner) + yellow + ' (Owns ' + str(item_owner_total) + ' total)')

###################################
# Get items for sale by attribute #
###################################

def parse_fs_by_attribute(_query_response):
    avax_price = get_avax_price()
    item_num = 0
    if len(_query_response) == 0:
        pred('\nNo Items Found')
    else:
        collection_info = requests.get('https://api.joepegs.dev/v2/collections/' + _query_response[0]['collection'], headers=headers).json()
        collection_floor = convert_ether(collection_info['floor'])
        collection_address = collection_info['address']
        total_items = len(_query_response)

        for item in _query_response:
            collection_name = item['collectionName']
            item_id = item['tokenId']
            item_ranking = item['rarityRanking']
            item_price = convert_ether(item['currentAsk']['price'])
            avax_difference = float(item_price) - float(collection_floor)
            usd_difference = avax_difference * avax_price
            item_bid = convert_ether(item['bestBid']['price'])
            item_sale_id = item['currentAsk']['id']
            item_num += 1
            pyellow('\nItem Number: ' + white + str(item_num))
            pblue('Collection Name: ' + white + collection_name + ' #' + str(item_id))
            if item_ranking == None:
                pblue('Item Ranking: ' + red + 'No Rarity Ranking')
            else:    
                pblue('Item Ranking: ' + white + str(item_ranking))
            pblue('Item Price: ' + white + str(item_price) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(item_price) * avax_price)) + ') ' + red + '[+ ' + str('%.2f' % avax_difference) + ' AVAX] ' + '[+ $' + str('%.2f' % usd_difference) + ' USD]')
            if item_bid == None:
                pblue('Item Highest Bid: ' + red + 'No Bids')
            else:
                pblue('Item Highest Bid: ' + white + str(item_bid) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(item_bid) * avax_price)) + ')' + red + ' [' + str('%.2f' % (float(item_bid) - float(item_price))) + ' AVAX] ' + '[$ ' + str('%.2f' % ((float(item_bid) - float(item_price)) * avax_price)) + ' USD]')
            pblue('Item URL: ' + white + 'https://joepegs.com/item/' + collection_address + '/' + str(item_id))
        
        pblue('\nTotal Items Found: ' + white + str(total_items))
        pblue('Collection Floor: ' + white + str(collection_floor) + ' AVAX' + yellow + ' ($' + str('%.2f' % (float(collection_floor) * avax_price)) + ')')


########################################
#  Get Specific Item Info by Attribute #
########################################        

def query_collection_fs_by_attribute(_collection_address, _encoded_attributes):
    response = requests.get('https://api.joepegs.dev/v2/items?collectionAddress=' + _collection_address + '&filters=buy_now&orderBy=price_asc&pageSize=100&attributeFilters=' + _encoded_attributes, headers=headers).json()
    return response

###############################
#   Encode attribute filter   #
###############################

def encode_attributes(_attribute, _attribute_value):
    attribute_filter = '[{"traitType": "' + _attribute + '", "values":["' + _attribute_value + '"]}]'
    _encoded_attributes = urllib.parse.quote(attribute_filter)
    return _encoded_attributes

################################
#    Get Collection Buy Now    #
################################  

def list_collection_buy_now(collection_address, encoded_attributes):
    query = 'https://api.joepegs.dev/v2/items?filters=buy_now&orderBy=rarity_desc&collectionAddress=' + collection_address + '&attributeFilters=' + encoded_attributes
    collection_listed = requests.get(query, headers=headers).json()
    return collection_listed

##################################
#    Get Collection Attributs    #
##################################

def get_collection_attributes(_collection_address):
    collection_attributes = requests.get('https://api.joepegs.dev/v2/collections/' + _collection_address, headers=headers).json()
    pyellow('\n' + collection_attributes['name'] + ' Attributes:')
    for attribute in collection_attributes['attributes']:
        pblue('Attribute: ' + white + attribute['traitType'])

###################################
#    Get Collection Overview      #
###################################

def get_collection_overview(collection_address):
    collection_overview = requests.get('https://api.joepegs.dev/v2/collections/' + collection_address, headers=headers).json()
    return collection_overview

####################################
#      Get Attribute Types         #
####################################
#NOTE:
# - Allow users to input numbers to select attribute type

def get_values(_collection_address, _attribute):
    collection = get_collection_overview(_collection_address)
    collection_supply = collection['numItems']
    for trait_type in collection['attributes']:
        if trait_type['traitType'] == _attribute:
            pyellow('\n' + _attribute + ' Types:')
            for value in trait_type['values']:
                pblue('Type: ' + white + value['value'] + yellow + ' - ' + str(value['count']) + ' item(s)' + lgreen + ' [' + str('%.2f' % (float(value['count']) / float(collection_supply) * 100)) + '%]')
    
################################
#   Query User for Item Info   #
################################
#NOTE:
# - Add in functionality to allow searches with multiple attributes
# - Add in functionality to allow searches with multiple values for a single attribute
    
def get_collection_by_attribute():
    pblue('\nSearch by Attribute')
    collection_address = get_collection_address_user()
    get_collection_attributes(collection_address)
    attribute = get_attribute()
    get_values(collection_address, attribute)
    attribute_value = get_attribute_value()
    encoded_attribute = encode_attributes(attribute, attribute_value)
    return collection_address, encoded_attribute

###############################################
#    Scan for NFTs based off of attributes    #
###############################################

def scan_attributes(collection_address, encoded_attributes, scan_interval, is_buy, want_alert, max_price):
    currently_listed = list_collection_buy_now(collection_address, encoded_attributes)
    if len(currently_listed) > 0:
        for item in currently_listed:
            if convert_ether(item['currentAsk']['price']) <= max_price:
                ask_id = item['currentAsk']['id']
                item_collection = item['collectionName']
                item_collection_id = item['tokenId']
                item_price = convert_ether(item['currentAsk']['price'])
                item_rarity = item['rarityRanking']
                item_img = item['metadata']['image']
                item_pfp = item['collectionPfpUrl']
                if want_alert == True and is_buy == False:
                    discord_alert(item_collection, item_price, item_rarity, item_img, item_collection_id, item_pfp)
                if want_alert == True and is_buy == True:
                    discord_alert(item_collection, item_price, item_rarity, item_img, item_collection_id, item_pfp)
                    purchase_nft(ask_id, item_price)
    else:
        pred('No listings found')

    pyellow('\nScanning...')
    time.sleep(float(scan_interval))
    scan_attributes(collection_address, encoded_attributes, scan_interval, is_buy, want_alert, max_price)