# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:57:15 2022

@author: Shiv Muthukumar

ALLOWS TO IMPORT CRYPTO DATA USING API AND CREATING A HEAT MAP OF THEIR CORRELATION

"""

import requests
import datetime
import seaborn as sns
import pandas as pd


def combine_crypto_dfs(df_main, df_add):
    # COMBINES TWO DATAFRAME INTO ONE GIVEN THE DATES
    # ASSUMPTION - ALL DF_ADD COINS HAVE DATA FOR ALL DATES IN DF_MAIN
    return pd.merge(df_main, df_add, on='Dates', how='outer')


class Crypto_Coin:
    # KEEPS A RECORD OF THE OBJECTS CREATED
    _registry = []
    
    def __init__(self, name, currency='usd', days=30, interval='daily'):
        self._registry.append(self)
        self.name=name
        self.currency=currency
        self.days=days
        self.interval=interval
        self.__get_crypto_data()
        self.__extract_dates_and_prices()
        
    def __get_crypto_data(self):
        # GETS THE DATA FROM THE API LINK AND CONVERTS THE DATA TO JSON FORMAT
        url="https://api.coingecko.com/api/v3/coins/"+self.name+"/market_chart?vs_currency="+self.currency+"&days="+str(self.days)+"&interval="+self.interval
        self.crypto_data = requests.get(url).json()
        
    def __extract_dates_and_prices(self):
        # EXTRACTS THE DATES AND PRICES, FORMATS, AND CREATE A DATAFRAME
        prices=[i[1] for i in self.crypto_data['prices']]
        dates=[datetime.datetime.fromtimestamp(i[0]/1000).strftime('%Y-%m-%d') for i in self.crypto_data['prices']]
        self.df = pd.DataFrame(dates, columns=['Dates'])
        self.df[self.name+'_price'] = prices
        
# DECLARE THE COINS REQUIRED AS OBJECTS USING THE CLASS
solana=Crypto_Coin('solana')
binance=Crypto_Coin('binancecoin')
bitcoin=Crypto_Coin('bitcoin')
ethereum=Crypto_Coin('ethereum')

# COMBINES ALL THE COIN OBJECTS' DATA TO CREATE A SINGLE DATAFRAME OF THEIR PRICES
crypto_list = Crypto_Coin._registry
df = crypto_list[0].df
for coin in crypto_list[1:]:
    df = combine_crypto_dfs(df, coin.df)
    
# USES THE SEABORN PACKAGE TO CREATE A HEATMAT OF THE PRICES' CORRELATION 
sns.heatmap(df.corr(), cmap="gray_r")
