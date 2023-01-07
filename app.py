import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

spot_client = Client(key, secret)
response = spot_client.avg_price("SOLUSDT")
if response:
  avg_time = response['mins']
  avg_price = response['price']

print("SOL avg_price: ", avg_price, "in", avg_time, "mins")