import json
import os
import time
from datetime import datetime
from unittest import TestCase

from rstms_etherscan_python import Etherscan
from rstms_etherscan_python.exceptions import (
    EtherscanErrorResponse,
    EtherscanUnauthorizedEndpoint,
)

CONFIG_PATH = "rstms_etherscan_python/configs/{}-stable.json"
API_KEY = os.environ["API_KEY"]  # Encrypted env var by Travis

TEST_API_PRO_ENDPOINTS = "TEST_API_PRO_ENDPOINTS" in os.environ


def test_init():
    api = Etherscan(API_KEY)
    assert api


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


def dump(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)


class Case(TestCase):
    _MODULE = ""
    # _NETS = ["MAIN", "KOVAN", "RINKEBY", "ROPSTEN", "GOERLI"]
    _NETS = ["MAIN", "GOERLI"]

    def methods(self, net):
        print(f"\nNET: {net}")
        print(f"MODULE: {self._MODULE}")
        config = load(CONFIG_PATH.format(net))
        etherscan = Etherscan(API_KEY, net)
        for fun, v in config.items():
            if not fun.startswith("_"):  # disabled if _
                if v["module"] == self._MODULE:
                    try:
                        res = getattr(etherscan, fun)(**v["kwargs"])
                        rtype = type(res)
                    except EtherscanUnauthorizedEndpoint as exc:
                        if TEST_API_PRO_ENDPOINTS:
                            raise exc from exc
                        else:
                            rtype = type(exc)
                            res = repr(exc)
                    except EtherscanErrorResponse as exc:
                        rtype = type(exc)
                        res = repr(exc)

                    print(f"METHOD: {fun}, RTYPE: {rtype}")
                    # Create log files (will update existing ones)
                    fname = f"logs/standard/{net}-{fun}.json"
                    log = {
                        "method": fun,
                        "module": v["module"],
                        "kwargs": v["kwargs"],
                        "log_timestamp": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                        "res": res,
                    }
                    dump(log, fname)
                    time.sleep(0.5)

    def test_net_methods(self):
        for net in self._NETS:
            self.methods(net)


class TestAccounts(Case):
    _MODULE = "accounts"


class TestBlocks(Case):
    _MODULE = "blocks"


class TestContracts(Case):
    _MODULE = "contracts"


class TestGasTracker(Case):
    _MODULE = "gastracker"


class TestPro(Case):
    _MODULE = "pro"


class TestProxy(Case):
    _MODULE = "proxy"


class TestStats(Case):
    _MODULE = "stats"


class TestTokens(Case):
    _MODULE = "tokens"


class TestTransactions(Case):
    _MODULE = "transactions"
