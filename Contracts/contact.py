from web3 import Web3

# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))

# 代理合约地址
proxy_contract_address = Web3.to_checksum_address('0xB342e7D33b806544609370271A8D074313B7bc30')

# EIP-1967定义的实现合约地址的存储槽
implementation_slot = "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"

# 读取存储槽的值，即实现合约的地址
implementation_address = w3.eth.get_storage_at(proxy_contract_address, implementation_slot).hex()

# 确保地址是完整的40个字符长度
full_implementation_address = implementation_address[-40:]

# 转换为校验和地址
checksum_implementation_address = Web3.to_checksum_address('0x' + full_implementation_address)

print("实现合约地址:", checksum_implementation_address)
