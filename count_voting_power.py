from web3 import Web3
import csv
import sys
from ressources import *
from utils import balance_of
from utils import has_proxy
from utils import connect_chain
from utils import list_voters

# read in command line arguments
list_of_voters = sys.argv[1]
node = sys.argv[2]
poll_closing_block = int(sys.argv[3])

voters = list_voters(list_of_voters)
chain = connect_chain(node)


VOTING_POWER = 0

for voter in voters:

    MKRs_HOT = 0
    IOU_1_0 = IOU_1_1 = IOU_1_2 = 0
    STAKED_VIA_PROXY_1_1 = MKRs_1_1_COLD = 0
    STAKED_VIA_PROXY_1_2 = MKRs_1_2_COLD = 0

    """
    HOT STORAGE
    """
    # MKRs on hot wallet
    MKRs_HOT = balance_of(chain, MKR, voter, token_abi, poll_closing_block)

    """
    DIRECT STAKES
    """
    # MKRs staked directly to DSChief 1.0
    IOU_1_0 = balance_of(chain, IOU_1_0_address, voter, token_abi, poll_closing_block)

    # MKRs staked directly to DSChief 1.1
    IOU_1_1 = balance_of(chain, IOU_1_1_address, voter, token_abi, poll_closing_block)

    # MKRs staked directly to DSChief 1.2
    IOU_1_2 = balance_of(chain, IOU_1_2_address, voter, token_abi, poll_closing_block)

    """
    STAKES VIA VoteProxy; COLD STORAGE
    """
    if has_proxy(
        chain,
        voter,
        vote_proxy_factory_V1_address,
        vote_proxy_factory_V1_abi,
        poll_closing_block,
    ):

        vote_proxy_factory_V1 = chain.eth.contract(
            address=Web3.toChecksumAddress(vote_proxy_factory_V1_address),
            abi=vote_proxy_factory_V1_abi,
        )
        vote_proxy = vote_proxy_factory_V1.functions.hotMap(
            Web3.toChecksumAddress(voter)
        ).call(block_identifier=poll_closing_block)
        # MKRs staked to DSChief 1.1 via VoteProxy
        STAKED_VIA_PROXY_1_1 = balance_of(
            chain, IOU_1_1_address, vote_proxy, token_abi, poll_closing_block
        )

        vote_proxy_contract = chain.eth.contract(
            address=Web3.toChecksumAddress(vote_proxy), abi=vote_proxy_abi
        )

        # MKRs stored on linked cold wallet
        cold = vote_proxy_contract.functions.cold().call(
            block_identifier=poll_closing_block
        )
        if cold.lower() != voter.lower():
            MKRs_1_1_COLD = balance_of(chain, MKR, cold, token_abi, poll_closing_block)

    if has_proxy(
        chain,
        voter,
        vote_proxy_factory_V2_address,
        vote_proxy_factory_V2_abi,
        poll_closing_block,
    ):

        vote_proxy_factory_v2_contract = chain.eth.contract(
            address=Web3.toChecksumAddress(vote_proxy_factory_V2_address),
            abi=vote_proxy_factory_V2_abi,
        )
        vote_proxy = vote_proxy_factory_v2_contract.functions.hotMap(
            Web3.toChecksumAddress(voter)
        ).call(block_identifier=poll_closing_block)
        # MKRs staked to DSChief 1.2 via VoteProxy
        STAKED_VIA_PROXY_1_2 = balance_of(
            chain, IOU_1_2_address, vote_proxy, token_abi, poll_closing_block
        )

        vote_proxy_contract = chain.eth.contract(
            address=Web3.toChecksumAddress(vote_proxy), abi=vote_proxy_abi
        )

        # MKRs stored on linked cold wallet
        cold = vote_proxy_contract.functions.cold().call(
            block_identifier=poll_closing_block
        )
        if cold.lower() != voter.lower():
            MKRs_1_2_COLD = balance_of(chain, MKR, cold, token_abi, poll_closing_block)

    VOTING_POWER = (
        VOTING_POWER
        + MKRs_HOT
        + IOU_1_0
        + IOU_1_1
        + IOU_1_2
        + STAKED_VIA_PROXY_1_1
        + MKRs_1_1_COLD
        + STAKED_VIA_PROXY_1_2
        + MKRs_1_2_COLD
    )

print(
    {
        "VOTERS": len(voters),
        "POLL CLOSING BLOCK": poll_closing_block,
        "VOTING POWER": VOTING_POWER,
    }
)
