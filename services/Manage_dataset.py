

import asyncio
from datetime import datetime
from time import sleep as sec
from binance.client import AsyncClient, Client
import pandas as pd
from dotenv import load_dotenv
import os

# This loads the .env file that resides in the same directory as the script.
env_path = os.path.join(os.path.dirname(__file__), 'bin', '.env')
load_dotenv(dotenv_path=env_path)


api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')


class ManageData:
    def __init__(self, api_key="", api_secret="", interval='15m'):
        self.client = Client(api_key=api_key, api_secret=api_secret)
        self.__intervals = {
            '15m': Client.KLINE_INTERVAL_15MINUTE,
            '1h': Client.KLINE_INTERVAL_1HOUR,
            '4h': Client.KLINE_INTERVAL_4HOUR,
            '1d': Client.KLINE_INTERVAL_1DAY
        }
        self.interval = self.__intervals.get(interval)
        self.dataset = pd.DataFrame()

    def get_binance_data(self, start='1 Jan 2024', end=None, symbol="ETHUSDT"):
        print(f'Historical interval {self.interval}')
        klines = self.client.get_historical_klines(
            symbol=symbol, interval=self.interval, start_str=start, end_str=end)
        return self.prepare_data(klines)

    def prepare_data(self, klines):
        data = pd.DataFrame(klines)
        data.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume',
                        'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol', 'ignore']
        data['time_th'] = pd.to_datetime(data['open_time'], unit='ms').dt.tz_localize(
            'UTC').dt.tz_convert('Asia/Bangkok').dt.strftime('%H:%M:%S')
        data.index = [pd.to_datetime(x, unit='ms').strftime(
            '%Y-%m-%d %H:%M:%S') for x in data.open_time]
        float_columns = ['open', 'high', 'low', 'close', 'volume']
        data[float_columns] = data[float_columns].astype(float)
        self.dataset = data
        print(data)
        usecols = ['open', 'close', 'high', 'low', 'volume', 'time_th']
        return data[usecols]
    def get_data(self):
        return self.dataset

class ExportData():
    def __init__(self,symbol="ETHUSDT",dataset=[]) -> None:
        self.symbol = symbol
        self.name = date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        self.dataset =dataset
        self.createdirectory()
        
        pass
    def createdirectory(self,path_ex=False):
        path_ex = {path_ex if type(path_ex) !=bool else ""}
        coins_history_path = f"dataset/"
        indicators_path = f"indicators/{self.symbol}"
        try:
            os.makedirs(coins_history_path, exist_ok=True)
            os.makedirs(indicators_path, exist_ok=True)
        except:
            pass    
    def exportdata(self):
        pass
    
if __name__ == "__main__":
    
    manage = ManageData(api_key=api_key, api_secret=api_secret)
    coins_history = manage.get_binance_data()
    coins_history.head()
    ExportData()
    