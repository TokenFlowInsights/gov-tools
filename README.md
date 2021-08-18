# gov-tools

### Requirements:

* Python 3.8+
* Web3.py
* Access to ethereum node

### Parameters
* List of voters (.csv file) - e.g. all addresses that voted for a specific option
* Node address - URL for Ethereum node RPC calls
* Ethereum block number - block for which the total Voting Power is calculated

### How-to

1. Install Python >= 3.8:
    https://www.python.org/downloads/


2. Install web3:
    ```sh
    $ pip install web3
    ```

3. Get access to ethereum node (e.g. by using https://www.alchemy.com/)
   > URL may look like this: https://eth-mainnet.alchemyapi.io/v2/AaaAaAAa1AaaaA-1A-AAAAA_AaAA1aaA

    Alternative providers of node services: https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/


4. Prepare a list of voters in CSV file format (one address in a row, no header). Save the .csv file in gov-tools directory.


5. Select a block number for which you want to count the total Voting Power.


6. You're all set and ready to launch the script:

    ```sh
    $ python count_voting_power.py <file.csv> <HTTP node address> <ethereum block>
    ```

    Example:
    ```sh
    $ python count_voting_power.py voters.csv https://eth-mainnet.alchemyapi.io/v2/AaaAaAAa1AaaaA-1A-AAAAA_AaAA1aaA 13048140
    ```
   