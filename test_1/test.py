import web3
from web3 import Web3

# bsc testnet network
# https://data-seed-prebsc-1-s1.bnbchain.org:8545
# 获取测试网地址的方法
# https://cointool.app/rpcServer/cosmos?name=injective
# https://chainlist.org/chain/1
#bsc_test = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.bnbchain.org:8545'))
#bsc_main = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
#print(f'testnet is connect {bsc_test.is_connected()}')
#print(f'mainnet is connect {bsc_main.is_connected()}')
# 在测试网中，货币通常是免费提供的，通常是一个叫“faucet”水龙头的东西来进行货币提供
# https://www.bnbchain.org/en/testnet-faucet  bnb链可以通过这个网址来领取，手动也好
#bsc_main.eth.get_block("latest")
#bsc_test.eth.get_block("latest")
eth_test = Web3(Web3.HTTPProvider('https://rpc.sepolia.org/'))
print(eth_test.is_connected())
print(eth_test.eth.get_block('latest'))