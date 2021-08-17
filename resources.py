TOKEN_ABI = """
    [
        {"constant": true,"inputs": [],"name": "decimals","outputs": [{"internalType": "uint8","name": "","type": "uint8"}],"payable": false,"stateMutability": "view","type": "function"},
        {"constant": true,"inputs": [],"name": "symbol","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},
        {"constant":true,"inputs":[{"name":"src","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}
    ]
"""

VOTE_PROXY_FACTORY_V1_ABI = """
    [
        {"constant":false,"inputs":[],"name":"linkSelf","outputs":[{"name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"hot","type":"address"}],"name":"initiateLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"name":"guy","type":"address"}],"name":"hasProxy","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"hotMap","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"linkRequests","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"breakLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"coldMap","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"cold","type":"address"}],"name":"approveLink","outputs":[{"name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"inputs":[{"name":"chief_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"name":"cold","type":"address"},{"indexed":true,"name":"hot","type":"address"}],"name":"LinkRequested","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"name":"cold","type":"address"},{"indexed":true,"name":"hot","type":"address"},{"indexed":true,"name":"voteProxy","type":"address"}],"name":"LinkConfirmed","type":"event"}
    ]
"""

VOTE_PROXY_FACTORY_V2_ABI = """
    [
        {"inputs":[{"internalType":"address","name":"chief_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"cold","type":"address"},{"indexed":true,"internalType":"address","name":"hot","type":"address"},{"indexed":true,"internalType":"address","name":"voteProxy","type":"address"}],"name":"LinkConfirmed","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"cold","type":"address"},{"indexed":true,"internalType":"address","name":"hot","type":"address"}],"name":"LinkRequested","type":"event"},
        {"constant":false,"inputs":[{"internalType":"address","name":"cold","type":"address"}],"name":"approveLink","outputs":[{"internalType":"contract VoteProxy","name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[],"name":"breakLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"internalType":"contract ChiefLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"coldMap","outputs":[{"internalType":"contract VoteProxy","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"hasProxy","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"hotMap","outputs":[{"internalType":"contract VoteProxy","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"internalType":"address","name":"hot","type":"address"}],"name":"initiateLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"linkRequests","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"linkSelf","outputs":[{"internalType":"contract VoteProxy","name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"}
    ]
"""

VOTE_PROXY_ABI = """
    [
        {"constant":true,"inputs":[],"name":"gov","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[],"name":"cold","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"freeAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"iou","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"hot","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"inputs":[{"name":"_chief","type":"address"},{"name":"_cold","type":"address"},{"name":"_hot","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}
    ]
"""

MKR = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"

IOUs = dict(
            IOU_1_0="0x9aed7a25f2d928225e6fb2388055c7363ad6727b",
            IOU_1_1="0x496c67a4ced9c453a60f3166ab4b329870c8e355",
            IOU_1_2="0xa618e54de493ec29432ebd2ca7f14efbf6ac17f7"
       )

VOTE_PROXY_FACTORIES = dict(
            V1=dict(address="0x868ba9aeaca5b73c7c27f3b01588bf4f1339f2bc", abi=VOTE_PROXY_FACTORY_V1_ABI, iou=IOUs['IOU_1_1']),
            V2=dict(address="0x6fcd258af181b3221073a96dd90d1f7ae7eec408", abi=VOTE_PROXY_FACTORY_V2_ABI, iou=IOUs['IOU_1_2'])
        )