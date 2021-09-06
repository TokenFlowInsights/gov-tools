import sys

from resources import MKR, VOTE_PROXY_FACTORIES
from utils import *

# read in command line arguments
list_of_voters = sys.argv[1]
node = sys.argv[2]
block = int(sys.argv[3]) if sys.argv[3] else None

voters = list_voters(list_of_voters)
chain = connect_chain(node)

# calculate the total voting power
VOTING_POWER = 0
TOTAL_HOT_BALANCE = 0
TOTAL_CHIEF_DEPOSITS = 0
TOTAL_PROXY_DEPOSITS = 0
TOTAL_COLD_BALANCE = 0

for hot_address in voters:
    """
    HOT STORAGE
    """
    # MKRs in the HOT wallet
    HOT_balance = balance_of(chain, MKR, hot_address, block)

    """
    DIRECT STAKES & DELEGATED VOTES
    """
    CHIEF_deposit = get_deposit(chain, hot_address, block)

    """
    STAKES VIA VoteProxy & COLD STORAGE
    """
    PROXY_deposit = 0
    COLD_balance = 0
    VOTE_PROXY_balance = 0

    # iterate over Proxy Factories
    for VOTE_PROXY_FACTORY in VOTE_PROXY_FACTORIES:

        _has_proxy = has_proxy(
            chain,
            hot_address,
            VOTE_PROXY_FACTORY["address"],
            VOTE_PROXY_FACTORY["abi"],
            block,
        )

        if _has_proxy:
            # if voter has a proxy get its parameters
            vote_proxy, vote_proxy_address, cold_address = get_proxy(
                chain,
                hot_address,
                VOTE_PROXY_FACTORY["address"],
                VOTE_PROXY_FACTORY["abi"],
                block,
            )

            # MKRs staked in DSChiefs via VoteProxy
            if vote_proxy_address:
                PROXY_deposit += get_deposit(chain, vote_proxy_address, block)
                VOTE_PROXY_balance += balance_of(chain, MKR, vote_proxy_address, block)

            # MKRs in the COLD wallet if it is different than the HOT wallet
            if cold_address:
                if cold_address.lower() != hot_address.lower():
                    COLD_balance += balance_of(chain, MKR, cold_address, block)

            # if voter has latest version of VoteProxy don't add voting power from older one
            break
    
    VOTING_POWER = (
        VOTING_POWER + HOT_balance + CHIEF_deposit + PROXY_deposit + COLD_balance + VOTE_PROXY_balance
    )

print(
    {
        "VOTERS": len(voters),
        "BLOCK": block,
        "VOTING POWER": VOTING_POWER,
    }
)
