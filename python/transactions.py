import os

from web3               import Web3
from dotenv             import load_dotenv
from web3.types         import TxParams
from joe_exchange       import JOEXCHANGE_ABI
from joe_auctionhouse   import JOEAUCTION_ABI
from web3.middleware    import geth_poa_middleware

load_dotenv()

###########
#   BUY   #
###########

def purchase_nft(ask_id, item_price):

    tx_guts: TxParams = {
        'type': 0x2,
        'chainId': w3.eth.chain_id,
        'gas': gas_limit,
        'maxFeePerGas': Web3.toWei(max_gas_in_gwei, 'gwei'),
        'maxPriorityFeePerGas': Web3.toWei(gas_tip_in_gwei, 'gwei'),
        'nonce': w3.eth.get_transaction_count(account.address),
        'value': Web3.toWei(int(item_price), 'wei'), 
    }

    order_tuple = (str(ask_id))

    purchase_function = exchange_contract.batchBuyWithAVAXAndWAVAX(order_tuple)
    purchase_tx = purchase_function.buildTransactions(tx_guts)

    signed_tx = w3.eth.account.sign_transaction(purchase_tx, account.privateKey)
    purchase_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_hash = w3.toHex(purchase_hash)
    purchase_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    pyellow('\nNFT PURCHASED\n')
    pyellow(purchase_receipt)

############
#   SELL   #
############

def list_nft(ask_id, item_price):
    pkey = os.getenv('PRIVATE_KEY')
    exchange_address = '0xaE079eDA901F7727D0715aff8f82BA8295719977' # Joepeg Exchange

    gas_limit = 300_000
    max_gas_in_gwei = 50
    gas_tip_in_gwei = 2

    account = Account.from_key(pkey)

    rpc_url = 'https://api.avax.network/ext/bc/C/rpc'
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    exchange_contract = w3.eth.contract(address=Web3.toChecksumAddress(exchange_address), abi=JOEXCHANGE_ABI)

    tx_guts: TxParams = {
        'type': 0x2,
        'chainId': w3.eth.chain_id,
        'gas': gas_limit,
        'maxFeePerGas': Web3.toWei(max_gas_in_gwei, 'gwei'),
        'maxPriorityFeePerGas': Web3.toWei(gas_tip_in_gwei, 'gwei'),
        'nonce': w3.eth.get_transaction_count(account.address),
        'value': Web3.toWei(int(item_price), 'wei'), 
    }

    order_tuple = (str(ask_id))

    purchase_function = exchange_contract.batchBuyWithAVAXAndWAVAX(order_tuple)
    purchase_tx = purchase_function.buildTransactions(tx_guts)

    signed_tx = w3.eth.account.sign_transaction(purchase_tx, account.privateKey)
    purchase_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_hash = w3.toHex(purchase_hash)
    purchase_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    pyellow('\nNFT LISTED\n')
    pyellow(purchase_receipt)