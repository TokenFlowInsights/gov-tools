# gov-tools

### Requirements:

* Python 3.8+
* Web3.py
* Access to ethereum node (eg. https://www.alchemy.com/)
* Set of voters (in .csv format)
* Ethereum block number


### How-to

Install Python >= 3.8:
    https://www.python.org/downloads/


Install web3:
```sh
$ pip install web3
```

Get access to ethereum node (you'll need a URL that will be used to establish connection to the node):
    https://www.alchemy.com/
    > URL will look like this: https://eth-mainnet.alchemyapi.io/v2/AaaAaAAa1AaaaA-1A-AAAAA_AaAA1aaA

    There are more providers of node services, here's a list: https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/


Prepare a list of voters that you would like to count voting power for. One address in a row, no header, CSV file format.
    Put the .csv file in gov-tools directory


Prepare block number. This tool will count voting power of set of voters form passeed .csv file.


Launch the script:
```sh
$ python count_voting_power.py <file.csv> <HTTP node address> <ethereum block>
```

Example:
```sh
$ python count_voting_power.py voters.csv https://eth-mainnet.alchemyapi.io/v2/AaaAaAAa1AaaaA-1A-AAAAA_AaAA1aaA 13048140
```