import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CyrrencyConvertion:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote.lower() == base.lower():
            raise ConvertionException(f'Невозможно перевести {quote.lower()} в {base.lower()}')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f'Введено несуществующее значение валюты {quote.lower()}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Введено несуществующее значение валюты {base.lower()}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionException(f'Введено некорректное значение суммы валюты {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base.lower()]]

        return total_base * amount