"""Spot Trading API for BingX.

This module provides a comprehensive API for interacting with BingX's spot trading features.
It includes functionalities for account management, market data retrieval, trade execution,
and wallet operations.

Classes:
    - `SpotAPI`: Combines `AccountAPI`, `MarketAPI`, `TradesAPI`, and `WalletAPI` to provide
      a unified interface for managing spot trading on BingX.
"""

from python_bingx.client.spot.account import AccountAPI
from python_bingx.client.spot.market import MarketAPI
from python_bingx.client.spot.trades import TradesAPI
from python_bingx.client.spot.wallet import WalletAPI


class SpotAPI(AccountAPI, MarketAPI, TradesAPI, WalletAPI):
    """API for managing spot trading on BingX.

    This class combines functionalities from `AccountAPI`, `MarketAPI`, `TradesAPI`, and `WalletAPI`
    to provide a unified interface for managing spot trading, including account data, market data,
    trade execution, and wallet operations.
    """
