import asyncio

from data_visualization     import visualize_attributes
from connection_status      import check_status_code
from colors                 import pred, pblue
from menu                   import menu, menu_options, get_collection_address_user, get_collection_item, get_interval, collections_info_options, alert_or_buy, get_max_price, get_max_ranked, get_scan_option
from utils                  import trending_collections, get_collection_by_attribute, query_collection_fs_by_attribute, parse_fs_by_attribute, scan_attributes, print_collection_overview, get_collection_overview, get_item_overview, parse_collection_attributes, parse_item_attributes, get_top_ranked, parse_top_items, scan_floor

#####################################
#   Collection info Menu decisions  #
#####################################

async def select_collection_info_option():
    response = collections_info_options()
    if response == '1':
        collection_address = get_collection_address_user()
        query_response = get_collection_overview(collection_address)
        collection_attributes = query_response['attributes']
        collection_supply = query_response['numItems']
        print_collection_overview(query_response)
        parse_collection_attributes(collection_attributes, collection_supply)
        pblue('\nWhat else would you like to do?')
        await select_collection_info_option()
    elif response == '2':
        collection_address = get_collection_address_user()
        item_id = get_collection_item()
        query_response = get_item_overview(collection_address, item_id)
        collection_attributes = query_response['metadata']['attributes']
        parse_item_attributes(collection_attributes)
        pblue('\nWhat else would you like to do?')
        await select_collection_info_option()
    elif response == '3':
        [collection_address, encoded_attributes] = get_collection_by_attribute()
        query_response = query_collection_fs_by_attribute(collection_address, encoded_attributes)
        parse_fs_by_attribute(query_response)
        pblue('\nWhat else would you like to do?')
        await select_collection_info_option()
    elif response == '4':
        user_choice = get_scan_option()
        if user_choice == '1':
            [collection_address, encoded_attributes] = get_collection_by_attribute()
            scan_interval = get_interval()
            max_price = float(get_max_price())
            scan_attributes(collection_address, encoded_attributes, scan_interval, max_price)
        else:
            collection_address = get_collection_address_user()
            max_floor = get_max_price()
            scan_interval = get_interval()
            scan_floor(collection_address, max_floor, scan_interval)
    elif response == '5':
        collection_address = get_collection_address_user()
        query_response = get_collection_overview(collection_address)
        await visualize_attributes(query_response, collection_address)
        pblue('\nWhat else would you like to do?')
        await select_collection_info_option()
    elif response == '6':
        item_num = get_max_ranked()
        collection_address = get_collection_address_user()
        query_response = get_top_ranked(collection_address, item_num)
        parse_top_items(query_response, item_num)
        pblue('\nWhat else would you like to do?')
        await select_collection_info_option()
    elif response == '7':
        pblue('Exiting...')
        exit()
    else:
        pred('Invalid option selected')
        await select_collection_info_option()

############################
#   Start initial Prompt   #
############################

async def select_start_option():
    response = menu_options()
    if response == '1':
        check_status_code()
        await select_start_option()
    elif response == '2':
        trending_collections()
        await select_start_option()
    elif response == '3':
        await select_collection_info_option()
    elif response == '4':
        pblue('Exiting...')
        exit()
    else:
        pred('\nInvalid option selected')
        await select_start_option()

#########################
# How the Script Starts #
#########################

async def main():
    menu()

    await select_start_option()

asyncio.run(main())