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
