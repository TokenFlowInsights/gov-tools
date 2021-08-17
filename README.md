# gov-tools


Requirements:
---

* Python 3.8+
* Web3.py
* Access to ethereum node (eg. https://www.alchemy.com/)
* Set of voters (in .csv format)


Install web3:
```sh
$ pip install web3
```

Launch the script:
```sh
$ python count_voting_power.py <voters addresses in .csv format> <HTTP node address> <poll closing block>
```
