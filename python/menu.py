from colors import pblue, pyellow, pwhite, yellow, blue, white, pred

#####################
#      Menu Art     #
#####################

def menu():
    pblue('\n                  looter_')
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
    pblue('Flip NFTs on Joepegs' + '                  Version: ' + white + '1.0.0')
    pyellow('----------------------------------------------------')

#################################
#      Initial Menu Options     #
#################################

def menu_options():
    pyellow('\nPlease select an option:')
    pwhite('1) Test Connection')
    pwhite('2) Trending Collections')
    pwhite('3) Collection options')
    pwhite('4) Exit\n')
    response = input('Select option: ' + yellow)
    return response

#####################################
#      Collections options Menu     #
#####################################

def collections_info_options():
    pblue('\nSearch for a Collection\n')
    pyellow('Please select an option:')
    pwhite('1) Get Collection Overview')
    pwhite('2) View Item Info')
    pwhite('3) View Items based on Attribute')
    pwhite('4) Scan Options')
    pwhite('5) Visualize Collection Attribute Data')
    pwhite('6) Get Rarest Items (If Ranking is Available)')
    pwhite('7) Exit\n')
    response = input('Select option: ' + yellow)
    return response

###########################
#   Select Buy or Alert   #
###########################

def alert_or_buy():
    pyellow('\nIn response to finding listings, what should the script do?')
    pwhite('1) Alert me through Discord')
    pwhite('2) Attempt to purchase then Alert me through Discord')
    action = input('Select option: ' + yellow)
    return action

########################
#  Select Scan Option  #
########################

def get_scan_option():
    scan_type = ''
    pyellow('\nHow would you like to scan?')
    pwhite('1) Scan for new listings using an attribute')
    pwhite('2) Scan for new listings using a minimum floor price')
    scan_type = input('Select Option: '  + yellow)
    return scan_type

##########################################
#      User input Collection Address     #
##########################################

def get_collection_address_user():
    pyellow('\nPlease enter the collection Address:' + white)
    address = input('Enter Collection Address: ' + white)
    return address

###############################
#      User input Item ID     #
###############################

def get_collection_item():
    pyellow('\nPlease enter the collection Item ID:' + white)
    id_number = input('Enter Item ID: ' + white)
    return id_number

###########################################
#      User input Collection Attribute    #
###########################################

def get_attribute():
    pyellow('\nPlease enter the collection Attribute you want to look for:\n(Match Casing For Successful Query)' + white)
    attribute = input('Enter Attribute: ' + white)
    return attribute

###########################################
#         User input Attribute Value      #
###########################################

def get_attribute_value():
    pyellow('\nPlease enter the collection Attribute Type you want to look for:\n(Match Casing For Successful Query)' + white)
    attribute_value = input('Enter Attribute Value: ' + white)
    return attribute_value

#################################
#     Get Interval for Scan     #
#################################

def get_interval():
    pyellow('\nHow often should we scan for new listings?')
    interval = input('Enter Interval: ' + white)
    return interval

####################################
#     Get Maximum Buy Now Price    #
####################################

def get_max_price():
    pyellow('\nWhat is the highest price you want to filter for?')
    max_price = input('Enter Max Price (AVAX):' + white)
    return max_price

###################################
#     Get number of top ranked    #
###################################

def get_max_ranked():
    pyellow('\nHow many items would you like to see?')
    max_price = input('Enter Max items (up to 100):' + white)
    return max_price