import sys

from resources import MKR, VOTE_PROXY_FACTORIES
from utils import *

# read in command line arguments
list_of_voters = sys.argv[1]
node = sys.argv[2]
block = int(sys.argv[3]) if sys.argv[3] else None

voters = list()
for v in list_voters(list_of_voters):
    if v not in voters:
        voters.append(v)

chain = connect_chain(node)

# calculate the total voting power
VOTING_POWER = 0


for hot_address in voters:

    hot_address = hot_address.lower()
    """
    HOT STORAGE
    """
    # MKRs in the HOT wallet
    HOT_balance = balance_of(chain, MKR, hot_address, block)

    """
    DIRECT STAKES & DELEGATED VOTES
    """
    CHIEFS_deposit = get_deposit(chain, hot_address, block)

    """
    STAKES VIA VoteProxy & COLD STORAGE
    """
    PROXY_deposit = 0
    VOTE_PROXY_balance = 0
    COLD_deposit = 0
    COLD_balance = 0

    ADDRESSES = list()
    ADDRESSES.append(hot_address)

    # iterate over ProxyFactories
    for VOTE_PROXY_FACTORY in VOTE_PROXY_FACTORIES:

        _has_proxy = has_proxy(
            chain,
            hot_address,
            VOTE_PROXY_FACTORY["address"],
            VOTE_PROXY_FACTORY["abi"],
            block,
        )

        if _has_proxy:
            # if voter has VoteProxy get its parameters
            vote_proxy_address, cold_address = get_proxy(
                chain,
                hot_address,
                VOTE_PROXY_FACTORY["address"],
                VOTE_PROXY_FACTORY["abi"],
                block,
            )

            vote_proxy_address = (
                vote_proxy_address.lower() if vote_proxy_address else vote_proxy_address
            )
            cold_address = cold_address.lower() if cold_address else cold_address

            # MKRs staked to DSChief via VoteProxy
            # & MKRs stored in VoteProxy contract
            if vote_proxy_address and vote_proxy_address not in ADDRESSES:
                PROXY_deposit += get_chief_deposit(
                    chain,
                    VOTE_PROXY_FACTORY["chief_address"],
                    VOTE_PROXY_FACTORY["chief_abi"],
                    vote_proxy_address,
                    block,
                )
                VOTE_PROXY_balance += balance_of(chain, MKR, vote_proxy_address, block)
                ADDRESSES.append(vote_proxy_address)

            # MKRs in the COLD wallet if it is different than the HOT wallet
            if cold_address and cold_address not in ADDRESSES:
                COLD_balance += balance_of(chain, MKR, cold_address, block)
                ADDRESSES.append(cold_address)

            break

    VOTING_POWER = (
        VOTING_POWER
        + HOT_balance
        + CHIEFS_deposit
        + PROXY_deposit
        + VOTE_PROXY_balance
        + COLD_deposit
        + COLD_balance
    )

print(
    {
        "VOTERS": len(voters),
        "BLOCK": block,
        "VOTING POWER": VOTING_POWER,
    }
)
