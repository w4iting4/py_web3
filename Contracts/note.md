# 智能合约
## 基础概述
官方文档：https://ethereum.org/zh/smart-contracts  
智能合约解决传统合约中的信任问题，用官方文档的案例来说：  
>传统合约的最大问题之一是需要可信的个人来执行合约的结果。  
下面是一个例子：  
Alice 和 Bob 要进行一场自行车比赛。 假设 Alice 和 Bob 打赌 $10 元她会赢得比赛。 Bob 相信自己会成为赢家并同意下注。 最后，Alice 远远领先 Bob 完成了比赛，并且毫无疑问是赢家。 但 Bob 拒绝支付赌注，声称 Alice 一定是作弊了。  
这个荒唐的例子说明了所有非智能协议存在的问题。 即使协议条件得到满足（即你是比赛的获胜者），你仍然必须要信任对方会履行协议（即支付赌注）。  

## 什么是智能合约
>智能合约只是一个运行在以太坊链上的一个程序。 它是位于以太坊区块链上一个特定地址的一系列代码（函数）和数据（状态）。  
>
>智能合约也是一个以太坊帐户，我们称之为合约帐户。 这意味着它们有余额，可以成为交易的对象。 但是，他们无法被人操控，他们是被部署在网络上作为程序运行着。 个人用户可以通过提交交易执行智能合约的某一个函数来与智能合约进行交互。 智能合约能像常规合约一样定义规则，并通过代码自动强制执行。 默认情况下，您无法删除智能合约，与它们的交互是不可逆的。

官方将智能合约比喻成售卖机，钱 + 选择 = 产出对应内容， 就像自动售货机让厂商不再需要员工一样，智能合约可以在许多行业中取代中间人。  

## 属性
智能合约具备无需准入性、可组合性、局限性等多种特性。
无需准入性：任何人都可以部署智能合约  
可组合性: 智能合约在以太坊上公开，可以看成api，所以你可以在自己的合约中调用别人的合约
局限性: 智能合约无法获取现实世界相关的东西，举个例子，假设有一天区块链-淘宝交易平台诞生了，智能合约可以保证你付款了，但不能保证对方发货，因为那是现实世界的内容。而解决这个方案的主要方法是预言机。

## 多重签名合约
>多重签名合约是需要多个有效签名才能执行交易的智能合约帐户。 这对于避免持有大量以太币或其他代币的合约出现单点故障非常有用。 多重签名还可以在多方之间划分合同执行和密钥管理的责任，并防止丢失单个私钥导致不可逆转的资金损失。 由于这些原因，多重签名合约可用于简单的去中心化自治组织治理。 多重签名需要 M 个可能的可接受签名中的 N 个签名才能执行（其中 N ≤ M，并且 M > 1）。 普遍使用 N = 3, M = 5 和 N = 4, M = 7。 4/7 多重签名需要七个可能的有效签名中的四个。 这意味着即使失去了三个签名，资金仍然可以收回。 在这种情况下，这也意味着必须得到大多数密钥持有人的同意和签名才能执行合约。  

## ABI
智能合约的基础内容在上面粗略的讲了一下，我们最终的目的是与智能合约进行交互，那么我们该如何获取到这个接口的相关信息呢？  
以太坊虚拟机我理解类似与jvm，需要将solidity进行编译，随后再部署上evm进行运行。  
编译之后，编译器会生成 应用程序二进制接口(ABI),以方便你的应用程序能够理解合约并且调用合约的功能。  
ABI是什么？  
ABI是一份json文件，描述了部署的合约以及这个合约的函数，在web2和web3之间架起了沟通的桥梁。我们可以通过web2网络变成来调取web3的abi接口达到与合约交互的目的。  
一般来说是js读取abi，随后代码调用abi。下面是erc-20代币合约的abi文件：
```python
[
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_spender",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_from",
        "type": "address"
      },
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      },
      {
        "name": "_spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "payable": true,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  }
]
```
这里是sodility到abi的映射说明：https://docs.soliditylang.org/en/v0.7.0/abi-spec.html  
### abi的组成
函数（Functions）： 描述了合约中可供外部调用的函数的接口，包括函数的名称、参数类型和顺序、返回值类型、函数的状态可变性（例如 view、pure、payable 等）等信息。  
事件（Events）： 描述了合约中发生的特定状态变化或重要操作的日志记录，包括事件的名称、参数类型和顺序、是否为匿名事件等信息。  
构造函数（Constructor）： 描述了合约的构造函数，即合约实例化时执行的初始代码，包括构造函数的参数类型和顺序等信息。  
回退函数（Fallback）： 描述了合约在接收以太币但没有匹配到任何函数调用时的默认行为，通常用于处理未知的函数调用或接收以太币的情况。  
对于上面erc20的abi，下方是大概的解释：
>每个条目的 type 属性：
函数的条目类型为 "function"，事件的条目类型为 "event"。 根据这个属性，您可以确定每个条目是描述一个函数还是一个事件。  
函数条目的属性：  
函数条目包括 "constant"、"inputs"、"name"、"outputs"、"payable" 和 "stateMutability" 这些属性。  
>- name 属性指定了函数的名称  
>- inputs 属性描述了函数的输入参数  
>- outputs 属性描述了函数的输出参数  
>- stateMutability 属性描述了函数的状态可变性（例如，"view" 表示只读函数，"nonpayable" 表示不接受以太币的支付等）

>事件条目的属性：  
事件条目包括 "anonymous"、"inputs" 和 "name" 这些属性。  
>- name 属性指定了事件的名称
>- inputs 属性描述了事件的参数
>- anonymous 属性指示了事件是否为匿名事件。  

## 如何从一次交互获取到合约abi
说来话长，上次有一个`checkin`方法我没找到abi。
![img.png](img.png)  
要解决这个问题，有两个解决方法。第一个方法是通过js来找abi的相关内容，可以在加载的js中，搜索这个函数名称。  
那么直接找到加载的js，搜索这个`checkin`方法.
![img_1.png](img_1.png)  
第二个方法，去合约浏览器搜索交易的目的地址，那就是合约地址。点击`Contract`,往下划可以找到`abi.json`
![img_2.png](img_2.png)
![img_3.png](img_3.png)  
但是在这个json中，我们没有找到对应的方法，这就比较好玩了。
>可能由几个原因造成：  
合约已更新，ABI未同步：如果合约代码在BNBScan上显示的是早期版本，而该合约后来进行了更新（例如添加了新的方法），但更新的ABI没有被上传到BNBScan，那么就会出现你所描述的情况。在这种情况下，合约实际上包含了“checkin”方法，但BNBScan上显示的ABI不是最新的。  
代理合约：如果该合约是一个代理合约，它可能会委托调用到另一个合约，这个被委托的合约包含了“checkin”方法。在这种情况下，即使在代理合约的ABI中看不到“checkin”方法，它仍然可以通过代理合约调用。  
前端直接与合约交互：在一些情况下，前端应用可能直接构建并发送特定的合约调用，而不依赖于公开的ABI。这种方法通常用于高级功能或特定情况下的调用。  
BNBScan的数据延迟或错误：有时候，区块链浏览器可能会出现数据同步延迟或错误，导致显示的信息不是最新或不完整。

所以这里我们可以考虑第二个方向，代理合约。判断一个智能合约是否是代理合约,可以访问合约的源代码，查找是否存在典型的代理合约模式，例如使用`delegatecall`的逻辑.我们找他是否实现`_IMPLEMENTATION_SLOT`.  
这样就可以找到存储库的地址，随后通过代码转换为代理后的合约地址就ok了。
![img_4.png](img_4.png)
```python
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

实现合约地址: 0xfA73332a85bA27eC445c65291E01aF15f726EA08
```
随后去浏览器找到这个实现合约的地址，反编译代码  
![img_5.png](img_5.png)  
![img_6.png](img_6.png)
## py与abi交互
通过区块链浏览器或者js找到了相关的abi之后，我们可以通过abi来确定需要交互的参数，但是啊，我们无法确定交互参数的具体内容，就需要js调试来找到最后的参数了。  
这里就各凭本事了。  































