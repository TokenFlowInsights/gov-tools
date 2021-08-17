from web3 import Web3
import csv


def balance_of(chain, token, address, abi, block=None):

    try:
        token_contract = chain.eth.contract(
            address=Web3.toChecksumAddress(token), abi=abi
        )
        if block:
            balance = token_contract.functions.balanceOf(
                Web3.toChecksumAddress(address)
            ).call(block_identifier=block)
        else:
            balance = token_contract.functions.balanceOf(
                Web3.toChecksumAddress(address)
            ).call()
        decimals = token_contract.functions.decimals().call()
        balance /= 10 ** decimals
    except Exception as e:
        print(e)
        balance = 0

    return balance


def has_proxy(chain, address, vote_proxy_factory, abi, block=None):

    try:
        vote_proxy_factory_contract = chain.eth.contract(
            address=Web3.toChecksumAddress(vote_proxy_factory), abi=abi
        )
        if block:
            proxy = vote_proxy_factory_contract.functions.hasProxy(
                Web3.toChecksumAddress(address)
            ).call(block_identifier=block)
        else:
            proxy = vote_proxy_factory_contract.functions.hasProxy(
                Web3.toChecksumAddress(address)
            ).call()
    except Exception as e:
        print(e)
        proxy = False

    return proxy


def connect_chain(http_hook=None):
    method = 'HTTP'
    provider = Web3.HTTPProvider
    hook = http_hook

    try:
        w3 = Web3(provider(hook, request_kwargs={'timeout': 60}))
        if w3.isConnected():
            print("Connected to %s: %s with latest block %d." % (method, hook, w3.eth.blockNumber))
            return w3
        else:
            print('%s connection to %s failed.' % (method, hook))
            return None
    except Exception as e:
        print("Error while connecting to chain.")
        print(e)


def list_voters(file):
    voters = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            voters.append(row[0])
    
    return voters
