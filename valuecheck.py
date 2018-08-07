# Checks for values of stock & crypto symbols using Alpha Vantage 

import os

from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint

import config

def test():
    cc = ForeignExchange(key=config.AV_API)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    pprint(data)
    value = data['5. Exchange Rate']
    print(f'${value}')

if __name__ == '__main__':
    test()
