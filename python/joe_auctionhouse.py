JOEAUCTION_ABI = """
[
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "address",
          "name": "previousAdmin",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "newAdmin",
          "type": "address"
        }
      ],
      "name": "AdminChanged",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "implementation",
          "type": "address"
        }
      ],
      "name": "Upgraded",
      "type": "event"
    },
    {
      "stateMutability": "payable",
      "type": "fallback"
    },
    {
      "inputs": [],
      "name": "admin",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newAdmin",
          "type": "address"
        }
      ],
      "name": "changeAdmin",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "implementation",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newImplementation",
          "type": "address"
        }
      ],
      "name": "upgradeTo",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newImplementation",
          "type": "address"
        },
        {
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
        }
      ],
      "name": "upgradeToAndCall",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "stateMutability": "payable",
      "type": "receive"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__AuctionAlreadyExists",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__CurrencyMismatch",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__DutchAuctionCannotSettleUnstartedAuction",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__DutchAuctionCreatorCannotSettle",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__DutchAuctionInvalidStartEndPrice",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCannotBidOnEndedAuction",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCannotBidOnUnstartedAuction",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCannotCancelWithExistingBid",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCannotSettleUnstartedAuction",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCannotSettleWithoutBid",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionCreatorCannotPlaceBid",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionInsufficientBidAmount",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionInvalidMinBidIncrementPct",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionInvalidRefreshTime",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__EnglishAuctionOnlyCreatorCanSettleBeforeEndTime",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__ExpectedNonNullAddress",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__FeesHigherThanExpected",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__InvalidDropInterval",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__InvalidDuration",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__InvalidMinPercentageToAsk",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__InvalidStartTime",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__NoAuctionExists",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__OnlyAuctionCreatorCanCancel",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "JoepegAuctionHouse__UnsupportedCurrency",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "PendingOwnableUpgradeable__NoPendingOwner",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "PendingOwnableUpgradeable__NotOwner",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "PendingOwnableUpgradeable__NotPendingOwner",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "PendingOwnableUpgradeable__PendingOwnerAlreadySet",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "SafeAccessControlEnumerableUpgradeable__RoleIsDefaultAdmin",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "SafeAccessControlEnumerableUpgradeable__SenderMissingRoleAndIsNotOwner",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "SafePausableUpgradeable__AlreadyPaused",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "SafePausableUpgradeable__AlreadyUnpaused",
      "type": "error"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "oldCurrencyManager",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newCurrencyManager",
          "type": "address"
        }
      ],
      "name": "CurrencyManagerSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "caller",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        }
      ],
      "name": "DutchAuctionCancel",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "buyer",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "DutchAuctionSettle",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "startPrice",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "endPrice",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint96",
          "name": "startTime",
          "type": "uint96"
        },
        {
          "indexed": false,
          "internalType": "uint96",
          "name": "endTime",
          "type": "uint96"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "dropInterval",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "DutchAuctionStart",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "caller",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        }
      ],
      "name": "EnglishAuctionCancel",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "oldEnglishAuctionMinBidIncrementPct",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "newEnglishAuctionMinBidIncrementPct",
          "type": "uint256"
        }
      ],
      "name": "EnglishAuctionMinBidIncrementPctSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "bidder",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "bidAmount",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint96",
          "name": "endTimeExtension",
          "type": "uint96"
        }
      ],
      "name": "EnglishAuctionPlaceBid",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint96",
          "name": "oldEnglishAuctionRefreshTime",
          "type": "uint96"
        },
        {
          "indexed": true,
          "internalType": "uint96",
          "name": "newEnglishAuctionRefreshTime",
          "type": "uint96"
        }
      ],
      "name": "EnglishAuctionRefreshTimeSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "buyer",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "EnglishAuctionSettle",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "startPrice",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint96",
          "name": "startTime",
          "type": "uint96"
        },
        {
          "indexed": false,
          "internalType": "uint96",
          "name": "endTime",
          "type": "uint96"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "EnglishAuctionStart",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "pendingOwner",
          "type": "address"
        }
      ],
      "name": "PendingOwnerSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "oldProtocolFeeManager",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newProtocolFeeManager",
          "type": "address"
        }
      ],
      "name": "ProtocolFeeManagerSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "oldProtocolFeeRecipient",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newProtocolFeeRecipient",
          "type": "address"
        }
      ],
      "name": "ProtocolFeeRecipientSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": true,
          "internalType": "bytes32",
          "name": "previousAdminRole",
          "type": "bytes32"
        },
        {
          "indexed": true,
          "internalType": "bytes32",
          "name": "newAdminRole",
          "type": "bytes32"
        }
      ],
      "name": "RoleAdminChanged",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleGranted",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleRevoked",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "oldRoyaltyFeeManager",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newRoyaltyFeeManager",
          "type": "address"
        }
      ],
      "name": "RoyaltyFeeManagerSet",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "collection",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "royaltyRecipient",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "RoyaltyPayment",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "DEFAULT_ADMIN_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "PAUSER_ADMIN_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "PAUSER_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "PERCENTAGE_PRECISION",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "UNPAUSER_ADMIN_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "UNPAUSER_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "WAVAX",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "becomeOwner",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "cancelDutchAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "cancelEnglishAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "currencyManager",
      "outputs": [
        {
          "internalType": "contract ICurrencyManager",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "dutchAuctions",
      "outputs": [
        {
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "startTime",
          "type": "uint96"
        },
        {
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "endTime",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "endPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "dropInterval",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "emergencyCancelDutchAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "emergencyCancelEnglishAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "englishAuctionMinBidIncrementPct",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "englishAuctionRefreshTime",
      "outputs": [
        {
          "internalType": "uint96",
          "name": "",
          "type": "uint96"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "englishAuctions",
      "outputs": [
        {
          "internalType": "address",
          "name": "creator",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "startTime",
          "type": "uint96"
        },
        {
          "internalType": "address",
          "name": "lastBidder",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "endTime",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "lastBidPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "getDutchAuctionSalePrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        }
      ],
      "name": "getRoleAdmin",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "uint256",
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "getRoleMember",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        }
      ],
      "name": "getRoleMemberCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "grantRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "hasRole",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_englishAuctionMinBidIncrementPct",
          "type": "uint256"
        },
        {
          "internalType": "uint96",
          "name": "_englishAuctionRefreshTime",
          "type": "uint96"
        },
        {
          "internalType": "address",
          "name": "_currencyManager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_protocolFeeManager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_royaltyFeeManager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_protocolFeeRecipient",
          "type": "address"
        }
      ],
      "name": "initialize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        },
        {
          "internalType": "bytes",
          "name": "",
          "type": "bytes"
        }
      ],
      "name": "onERC721Received",
      "outputs": [
        {
          "internalType": "bytes4",
          "name": "",
          "type": "bytes4"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pendingOwner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "placeEnglishAuctionBid",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_wavaxAmount",
          "type": "uint256"
        }
      ],
      "name": "placeEnglishAuctionBidWithAVAXAndWAVAX",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "protocolFeeManager",
      "outputs": [
        {
          "internalType": "contract IProtocolFeeManager",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "protocolFeeRecipient",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "renounceRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "revokePendingOwner",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "revokeRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "royaltyFeeManager",
      "outputs": [
        {
          "internalType": "contract IRoyaltyFeeManager",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "contract IERC20",
          "name": "_currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "_startTime",
          "type": "uint96"
        },
        {
          "internalType": "uint96",
          "name": "_duration",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "_dropInterval",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_endPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "scheduleDutchAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "contract IERC20",
          "name": "_currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "_startTime",
          "type": "uint96"
        },
        {
          "internalType": "uint96",
          "name": "_duration",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "_startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "scheduleEnglishAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "pendingOwner_",
          "type": "address"
        }
      ],
      "name": "setPendingOwner",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "settleDutchAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "settleDutchAuctionWithAVAXAndWAVAX",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "settleEnglishAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "contract IERC20",
          "name": "_currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "_duration",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "_dropInterval",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_endPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "startDutchAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "contract IERC721",
          "name": "_collection",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "contract IERC20",
          "name": "_currency",
          "type": "address"
        },
        {
          "internalType": "uint96",
          "name": "_duration",
          "type": "uint96"
        },
        {
          "internalType": "uint256",
          "name": "_startPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_minPercentageToAsk",
          "type": "uint256"
        }
      ],
      "name": "startEnglishAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes4",
          "name": "interfaceId",
          "type": "bytes4"
        }
      ],
      "name": "supportsInterface",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_currencyManager",
          "type": "address"
        }
      ],
      "name": "updateCurrencyManager",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_englishAuctionMinBidIncrementPct",
          "type": "uint256"
        }
      ],
      "name": "updateEnglishAuctionMinBidIncrementPct",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint96",
          "name": "_englishAuctionRefreshTime",
          "type": "uint96"
        }
      ],
      "name": "updateEnglishAuctionRefreshTime",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_protocolFeeManager",
          "type": "address"
        }
      ],
      "name": "updateProtocolFeeManager",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_protocolFeeRecipient",
          "type": "address"
        }
      ],
      "name": "updateProtocolFeeRecipient",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_royaltyFeeManager",
          "type": "address"
        }
      ],
      "name": "updateRoyaltyFeeManager",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "userLatestAuctionNonce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "initialLogic",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "initialAdmin",
          "type": "address"
        },
        {
          "internalType": "bytes",
          "name": "_data",
          "type": "bytes"
        }
      ],
      "stateMutability": "payable",
      "type": "constructor"
    }
  ]
  """