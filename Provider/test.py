import web3
from web3 import Web3
from web3 import eth

# bsc testnet network
# https://data-seed-prebsc-1-s1.bnbchain.org:8545
# 获取测试网地址的方法
# https://cointool.app/rpcServer/cosmos?name=injective
# https://chainlist.org/chain/1
# bsc_test = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.bnbchain.org:8545'))
# bsc_main = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
# print(f'testnet is connect {bsc_test.is_connected()}')
# print(f'mainnet is connect {bsc_main.is_connected()}')
# 在测试网中，货币通常是免费提供的，通常是一个叫“faucet”水龙头的东西来进行货币提供
# https://www.bnbchain.org/en/testnet-faucet  bnb链可以通过这个网址来领取，手动也好
# bsc_main.eth.get_block("latest")
# bsc_test.eth.get_block("latest")
# eth_test = Web3(Web3.HTTPProvider('https://rpc.sepolia.org/'))
# print(eth_test.is_connected())
# print(eth_test.eth.get_block('latest'))
# w3 = Web3();
# acc = w3.eth.account.create();
# print(f'private key={w3. (acc.key)}, account={acc.address}')
# '''
#  private key=0x6807f8e3b44b762dcc00562373bb921be5c1adeab0e68baac77d375c4403eb9b, account=0x99E83432EF5a04b68d39Eda395d71BE25359BD18
# '''
eth_test = Web3(Web3.HTTPProvider('https://rpc.sepolia.org/'))
print(eth_test.is_connected())
#钱包地址方法
wallet_address = '0x99E83432EF5a04b68d39Eda395d71BE25359BD18'
print(Web3.is_address(wallet_address))
print(Web3.is_checksum_address(wallet_address))
print(Web3.to_checksum_address(wallet_address))
#获取当前钱包余额
balance = eth_test.eth.get_balance('0x99E83432EF5a04b68d39Eda395d71BE25359BD18')
print(f'当前地址 {wallet_address} 的余额是 {balance} wei')
print(f'当前地址 {wallet_address} 的余额是 {Web3.from_wei(balance,'ether')} e')
print(f'当前地址 {wallet_address} 的余额是 {Web3.from_wei(balance,'gwei')} gwei')