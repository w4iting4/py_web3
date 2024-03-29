import requests
from web3 import Web3, HTTPProvider
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.sessions import Session
# 抓不到包，别测试了  需要load yak的证书到到代码中进行 mitm
wallet_address1 = '0x99E83432EF5a04b68d39Eda395d71BE25359BD18'  # 有余额的测试地址
wallet_address1_pvk = '0x6807f8e3b44b762dcc00562373bb921be5c1adeab0e68baac77d375c4403eb9b'
wallet_address2 = '0x70f52bC5A11aDddcC1A149CB4096C1B41610c7C6'  # 新注册的地址
wallet_address2_pvk = '0x21e40cdcacc88dff289a1e4d635614601b724b961003729eae5bfe7327b0f0c7'

# 设置SOCKS代理
# proxy = 'socks5://127.0.0.1:8080'  # 替换为你的代理信息
session = Session()
session.proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# 使用重试机制
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))
print('1')
# 创建Web3实例并指定自定义的HTTPProvider
eth_test = Web3(HTTPProvider('https://rpc.sepolia.org/', session=session))
print(eth_test.is_connected())
# 你的代码...
# 1. Build a new tx
transaction = {
    'from': Web3.to_checksum_address(wallet_address1),
    'to': Web3.to_checksum_address(wallet_address2),
    'value': Web3.to_wei(0.1, 'ether'),
    'nonce': eth_test.eth.get_transaction_count(Web3.to_checksum_address(wallet_address1)),
    'gas': 200000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
    'chainId': eth_test.eth.chain_id
}

print("sign")
# 2. Sign tx with a private key
signed = eth_test.eth.account.sign_transaction(transaction, wallet_address1_pvk)
print("send tx")
# 3. Send the signed transaction
tx_hash = eth_test.eth.send_raw_transaction(signed.rawTransaction)
tx = eth_test.eth.get_transaction(tx_hash)
assert tx["from"] == Web3.to_checksum_address(wallet_address1)
