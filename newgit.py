import requests
import json
url = "https://www.cbr-xml-daily.ru/daily_json.js"
respons= requests.get((url))
data = json.loads(requests.text)
print(data)