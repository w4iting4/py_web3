import web3
from web3 import Web3

wallet_address1 = '0x99E83432EF5a04b68d39Eda395d71BE25359BD18'  # 有余额的测试地址
wallet_address1_pvk = '0x6807f8e3b44b762dcc00562373bb921be5c1adeab0e68baac77d375c4403eb9b'
wallet_address2 = '0x70f52bC5A11aDddcC1A149CB4096C1B41610c7C6'  # 新注册的地址
wallet_address2_pvk = '0x21e40cdcacc88dff289a1e4d635614601b724b961003729eae5bfe7327b0f0c7'

# 连接到测试网
eth_test = Web3(Web3.HTTPProvider('https://rpc.sepolia.org/'))
print(f'测试网连接: {eth_test.is_connected()}')
print(f'测试网的gasprice: {Web3.from_wei(eth_test.eth.gas_price,'gwei')} gwei')
# # 1. Build a new tx
# transaction = {
#     'from': Web3.to_checksum_address(wallet_address1),
#     'to': Web3.to_checksum_address(wallet_address2),
#     'value': Web3.to_wei(0.1,'ether'),
#     'nonce': eth_test.eth.get_transaction_count(Web3.to_checksum_address(wallet_address1)),
#     'gas': 200000,
#     'maxFeePerGas': 2000000000,
#     'maxPriorityFeePerGas': 1000000000
# #    'chainId':eth_test.eth.chain_id
# }
#
# # 2. Sign tx with a private key
# signed = eth_test.eth.account.sign_transaction(transaction, wallet_address1_pvk)
#
# # 3. Send the signed transaction
# tx_hash = eth_test.eth.send_raw_transaction(signed.rawTransaction)
# tx = eth_test.eth.get_transaction(tx_hash)
# assert tx["from"] == Web3.to_checksum_address(wallet_address1)

# 获取当前basefee
latest = eth_test.eth.get_block('latest')
basefee = latest['baseFeePerGas']
print(f'当前链上basefee的值为: {Web3.from_wei(basefee,'gwei')} gwei' )
