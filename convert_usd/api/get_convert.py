import requests


def converter(currency_out: str, currency_in: str, count: int):
    """В данной функции мы достаем две валюты для конвертации."""
    if count is None:
        count = 1
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    curse_usd = requests.get(url)
    res_valute_out = curse_usd.json().get('rates').get(currency_out)
    res_valute_in = curse_usd.json().get('rates').get(currency_in)
    if res_valute_in is None or res_valute_out is None:
        return 'Один из аргументов указан не верно'
    return round(res_valute_in / res_valute_out * float(count), 2)
