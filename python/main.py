from connection_status  import check_status_code, test_response
from colors             import pred, pblue
from menu               import menu, menu_options, get_collection_address_user, get_collection_item, get_collection_by_attribute
from utils              import collection_info, trending_collections

######################
#   Print menu Art   #
######################

menu()

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
        collection_info()
    elif response == '4':
        pblue('Exiting...')
        exit()
    else:
        pred('Invalid option selected')
        select_start_option()

select_start_option()

#####################################
#   Collection info Menu decisions  #
#####################################

def select_collection_info_option():
    response = collection_info()
    if response == '1':
        get_collection_address_user()
    elif response == '2':
        get_collection_item()
    elif response == '3':
        get_collection_by_attribute()
    elif response == '4':
        pblue('Exiting...')
        exit()
    else:
        pred('Invalid option selected')
        select_collection_info_option()