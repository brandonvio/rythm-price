import requests
import json
import urllib.parse
from src.EnvUtil import EnvUtil
# from src.KafkaUtil import KafkaUtil


# oanda_account_id = EnvUtil.get_env("OANDA_DEFAULT_ACCOUNT")
# oanda_stream_domain = EnvUtil.get_env("OANDA_STREAM_DOMAIN")
# oanda_token = EnvUtil.get_env("OANDA_TOKEN")
# oanda_instruments = urllib.parse.quote_plus(EnvUtil.get_env("INSTRUMENTS"))
# k = KafkaUtil()

oanda_account_id = ""
oanda_token = ""
oanda_stream_domain = "stream-fxtrade.oanda.com"
oanda_instruments = "EUR_USD,USD_JPY,AUD_USD,USD_CAD,USD_CHF,USD_JPY,EUR_JPY,GBP_USD"


def oanda_stream():
    headers = {"Authorization": f"Bearer {oanda_token}"}
    url = f"https://{oanda_stream_domain}/v3/accounts/{oanda_account_id}/pricing/stream?instruments={oanda_instruments}"
    price_stream = requests.get(url, stream=True, headers=headers)
    print(">>>> pricing service online! <<<<<")
    for line in price_stream.iter_lines():
        if line:
            line = json.loads(line.decode('utf-8'))
            # print(line)
            if line["type"] == "PRICE":
                publish_price_to_kafka(line)


def publish_price_to_kafka(line):
    price_dict = price_todict(line)
    # k.kafka_send(line)
    print(price_dict["time"], price_dict["instrument"], price_dict["bid"], price_dict["ask"])


def price_todict(line):
    ask = float(line["asks"][0]["price"])
    bid = float(line["bids"][0]["price"])
    mid = round(((ask + bid) / 2), 5)
    spread = round((ask - bid) * 10000, 2)
    return {
        "version": "1.01212244:802",
        "instrument": line["instrument"],
        "status": line["status"],
        "time": str(line["time"]),
        "tradeable": bool(line["tradeable"]),
        "ask": ask,
        "bid": bid,
        "mid": mid,
        "spread": spread,
        "ask_liquidity": int(line["asks"][0]["liquidity"]),
        "bid_liquidity": int(line["bids"][0]["liquidity"]),
        "ask_closeout": float(line["closeoutAsk"]),
        "bid_closeout": float(line["closeoutBid"])
    }
