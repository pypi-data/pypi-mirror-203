"""
etherscan-python

A minimal, yet complete, python API for etherscan.io.

forked from: https://github.com/pcko1/etherscan-python

"""

from .modules.accounts import Accounts as accounts
from .modules.blocks import Blocks as blocks
from .modules.contracts import Contracts as contracts
from .modules.gastracker import GasTracker as gastracker
from .modules.pro import Pro as pro
from .modules.proxy import Proxy as proxy
from .modules.stats import Stats as stats
from .modules.tokens import Tokens as tokens
from .modules.transactions import Transactions as transactions
from .version import __version__

__all__ = [
    "__version__",
    "accounts",
    "blocks",
    "contracts",
    "gastracker",
    "pro",
    "proxy",
    "stats",
    "tokens",
    "transactions",
]
