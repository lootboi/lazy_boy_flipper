from colors import pblue, pyellow, pwhite, yellow, blue, white

#####################
#      Menu Art     #
#####################

def menu():
    print()
    pblue('                  looter_')
    pblue('                    Y8888b,')
    pblue('                  ,oA8888888b,')
    pblue('            ,aaad8888888888888888bo')
    pblue('         ,d888888888888888888888888888b,')
    pblue('       ,88888888888' + yellow + ' LB FLIPPER ' + blue + '8888888888b,')
    pblue('      d8888888888888888888888888888888888888,')
    pblue('     d888888888888888888888888888888888888888b')
    pblue('    d888888P`                    `Y888888888888,')
    pblue('    88888P`                    Ybaaaa8888888888l')
    pblue('   a8888`                      `Y8888P` `V888888')
    pblue(' d8888888a                                `Y8888')
    pblue('AY/'' `\Y8b                                 ``Y8b')  
    pblue('Y`      `YP                                  ~~')
    pblue('`         `')
    pyellow('----------------------------------------------------')
    pblue('Flip NFTs on the AVAX network' + '         Version: ' + white + '1.0.0')
    pyellow('----------------------------------------------------')

#################################
#      Initial Menu Options     #
#################################

def menu_options():
    print()
    pyellow('Please select an option:')
    pwhite('1) Test Connection')
    pwhite('2) Trending Collections')
    pwhite('3) Search for Collection')
    pwhite('4) Exit')
    print()
    response = input('Select option: ')
    return response

#####################################
#      Collections options Menu     #
#####################################

def collections_info_options():
    print()
    pblue('Search for a collection')
    print()
    pyellow('Please select an option:')
    pwhite('1) View Collection Info')
    pwhite('2) View Specific Collection Item Info')
    pwhite('3) View collection Items based on attribute')
    pwhite('4) Exit')
    print()
    response = input('Select option: ')
    return response

##########################################
#      User input Collection Address     #
##########################################

def get_collection_address_user():
    print()
    pyellow('Please enter the collection Address:' + white)
    response = input('Enter Collection Address: ')
    return response

###############################
#      User input Item ID     #
###############################

def get_collection_item():
    print()
    pyellow('Please enter the collection Item ID:' + white)
    id_number = input('Enter Item ID: ')
    return id_number

###########################################
#      User input Collection Attribute    #
###########################################

def get_attribute():
    print()
    pyellow('Please enter the collection Attribute you want to look for:\n(Match Casing For Successful Query)' + white)
    attribute = input('Enter Attribute: ')
    return attribute

###########################################
#         User input Attribute Value      #
###########################################

def get_attribute_value():
    print()
    pyellow('Please enter the collection Attribute Type you want to look for:\n(Match Casing For Successful Query)' + white)
    attribute_value = input('Enter Attribute Value: ')
    return attribute_value
