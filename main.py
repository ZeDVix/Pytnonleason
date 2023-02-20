import requests
import json

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = json.loads(response.text)
Valute = str(input("""ВВедите акроним валюты, для удовства на экран выведен список акронимов:
Доллар США - USD,\n
Австралийский доллар - AUD\n
Канадский доллар - CAD\n
Швейцарский франк - CHF\n
Японская йена - JPY\n
Новозеландский доллар-NZD\n
Евро - EUR\n
Британский фунт - GBP\n
Шведская крона - SEK\n
Датская крона - DKK\n
Норвежская крона - NOK\n
Сингапурский доллар - SGD\n
Чешская крона - CZK\n
Гонконгский доллар - HKD\n
Мексиканский песо - MXN\n
Польский злотый - PLN\n
Российский рубль - RUB\n
Турецкая лира - TRY\n
Ранд ЮАР - ZAR\n
Китайский юань - CNH\n
ВВедите акроним интересующей вас валюты здесь:"""))
result = (data["Valute"][Valute]["Value"])
print("Курс на сегодня:",result)
# print(data)






