from django.conf import settings

import requests


def get_rates(base):
    try:
        url = 'https://openexchangerates.org/api/latest.json?app_id={ID}&base={base}'.format(
            ID=settings.OEG_API_ID,
            base=base
        )
        resp = requests.get(url)
        resp = resp.json()
        return resp['rates']
    except Exception as e:
        return print(e)