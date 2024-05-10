import asyncio
import time
from binance.client import AsyncClient,Client
import pandas as pd
from services import Manage_dataset


manage_data = Manage_dataset.ManageData()
Manage_dataset.ExportData(symbol="test")

if __name__ == "__main__":
    # asyncio.run(main())
    
    # dataset = pd.DataFrame.from_dict(dataset)
    # print(dataset)
    symbol = 'AXLUSDT'
    
    coin_data = manage_data.get_binance_data(symbol=symbol)
    
    print(coin_data)
    pass