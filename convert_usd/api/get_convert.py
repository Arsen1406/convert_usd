import requests


def converter(valute_out: str, valute_in: str, count: float) -> float:
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    curse_usd = requests.get(url)
    res_valute_out = curse_usd.json().get('rates').get(valute_out)
    res_valute_in = curse_usd.json().get('rates').get(valute_in)
    return res_valute_in / res_valute_out * count


