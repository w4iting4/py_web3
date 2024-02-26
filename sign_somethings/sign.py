import web3
from web3 import Web3
from eth_account.messages import encode_defunct

msg = "313 fuck free world"
wallet_address1 = '0x99E83432EF5a04b68d39Eda395d71BE25359BD18'  # 有余额的测试地址
wallet_address1_pvk = '0x6807f8e3b44b762dcc00562373bb921be5c1adeab0e68baac77d375c4403eb9b'  # 当前地址的私钥

eth_test = Web3(Web3.HTTPProvider('https://rpc.sepolia.org/'))
print(f'连接测试网: {"成功" if eth_test.is_connected() else "失败"}')

msg = encode_defunct(text=msg)
print(f'格式化后的msg {msg}')

signed_msg = eth_test.eth.account.sign_message(msg, wallet_address1_pvk)
print(f'签名后的msg {signed_msg}')
print(f'签名后的msg类型是 {type(signed_msg)}')

print(f'从消息中恢复的地址是: {eth_test.eth.account.recover_message(msg, signature=signed_msg.signature)}')

