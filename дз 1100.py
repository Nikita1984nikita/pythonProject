import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://bank.gov.ua"

    def get_exchange_rate(self):
        url = f"{self.base_url}/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        data = response.json()

        for currency in data:
            if currency["cc"] == "USD":
                exchange_rate = currency["rate"]
                return float(exchange_rate)

        raise ValueError("Курс доллара не найден")

    def convert_to_usd(self, amount):
        exchange_rate = self.get_exchange_rate()
        usd_amount = amount / exchange_rate
        return usd_amount


converter = CurrencyConverter()

currency_amount = float(input("Введите сумму в гривнах : "))

usd_amount = converter.convert_to_usd(currency_amount)

print("Сумма в долларах США:", usd_amount)
