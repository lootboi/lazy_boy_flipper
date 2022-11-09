from connection_status  import check_status_code, test_response
from colors             import pred, pblue
from menu               import menu, menu_options, get_collection_address_user, get_collection_item, get_interval, collections_info_options, alert_or_buy, get_max_price
from utils              import trending_collections, get_collection_by_attribute, query_collection_fs_by_attribute, parse_fs_by_attribute, scan_attributes

#####################################
#   Collection info Menu decisions  #
#####################################

def select_collection_info_option():
    response = collections_info_options()
    if response == '1':
        get_collection_address_user()
    elif response == '2':
        get_collection_item()
    elif response == '3':
        [collection_address, encoded_attributes] = get_collection_by_attribute()
        query_response = query_collection_fs_by_attribute(collection_address, encoded_attributes)
        parse_fs_by_attribute(query_response)
        pblue('\nWhat else would you like to do?')
        select_collection_info_option()
    elif response == '4':
        [collection_address, encoded_attributes] = get_collection_by_attribute()
        scan_interval = get_interval()
        action = alert_or_buy()
        max_price = float(get_max_price())
        if action == '1':
            scan_attributes(collection_address, encoded_attributes, scan_interval, False, True, max_price)
        if action == '2':
            scan_attributes(collection_address, encoded_attributes, scan_interval, True, True, max_price)
    elif response == '5':
        pblue('Exiting...')
        exit()
    else:
        pred('Invalid option selected')
        select_collection_info_option()

############################
#   Start initial Prompt   #
############################

def select_start_option():
    response = menu_options()
    if response == '1':
        check_status_code(test_response)
        select_start_option()
    elif response == '2':
        trending_collections()
        select_start_option()
    elif response == '3':
        select_collection_info_option()
    elif response == '4':
        pblue('Exiting...')
        exit()
    else:
        pred('\nInvalid option selected')
        select_start_option()

#########################
# How the Script Starts #
#########################

menu()
select_start_option()