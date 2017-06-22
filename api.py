import requests
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
data = {
"key":"trnsl.1.1.20170620T100056Z.1ba350c30d7e8f4d.afde14c882c923e492cdad8c49674fb244d84f51",
"text":"wie sind Sie",
"lang":"de-en"}

r = requests.get(url = url, params = data)

data = r.json()
print(data['text'])




