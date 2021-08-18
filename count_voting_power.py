import sys

from resources import MKR, IOUs, VOTE_PROXY_FACTORIES
from utils import *

# read in command line arguments
list_of_voters = sys.argv[1]
node = sys.argv[2]
block = int(sys.argv[3]) if sys.argv[3] else None

voters = list_voters(list_of_voters)
chain = connect_chain(node)

# calculate the total voting power
VOTING_POWER = 0

for hot_address in voters:
    """
    DELEGATE
    """
    DELEGATED_balance = get_delegated_power(chain, hot_address)

    """
    HOT STORAGE
    """
    # MKRs in the HOT wallet
    HOT_balance = balance_of(chain, MKR, hot_address, block)

    """
    DIRECT STAKES
    """
    # MKRs staked in DSChiefs by the HOT wallet
    CHIEFS_balance = sum(
        [balance_of(chain, IOU, hot_address, block) for IOU in IOUs.values()]
    )

    """
    STAKES VIA VoteProxy and COLD STORAGE
    """
    PROXY_CHIEFs_balance = 0
    COLD_balance = 0

    # iterate over Proxy Factories
    for VOTE_PROXY_FACTORY in VOTE_PROXY_FACTORIES.values():

        if has_proxy(
            chain,
            hot_address,
            VOTE_PROXY_FACTORY["address"],
            VOTE_PROXY_FACTORY["abi"],
            block,
        ):

            # if voter has a proxy get its parameters
            vote_proxy, vote_proxy_address, cold_address = get_proxy(
                chain,
                hot_address,
                VOTE_PROXY_FACTORY["address"],
                VOTE_PROXY_FACTORY["abi"],
                block,
            )

            # MKRs staked in DSChiefs via VoteProxy
            PROXY_CHIEFs_balance += balance_of(
                chain, VOTE_PROXY_FACTORY["iou"], vote_proxy_address, block
            )

            # MKRs in the COLD wallet if it is different than the HOT wallet
            if cold_address:
                if cold_address.lower() != hot_address.lower():
                    COLD_balance += balance_of(chain, MKR, cold_address, block)

    VOTING_POWER = (
        VOTING_POWER
        + HOT_balance
        + CHIEFS_balance
        + PROXY_CHIEFs_balance
        + COLD_balance
        + DELEGATED_balance
    )

print(
    {
        "VOTERS": len(voters),
        "BLOCK": block,
        "VOTING POWER": VOTING_POWER,
    }
)
