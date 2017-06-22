import requests
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
data = {
"key":"trnsl.1.1.20170620T100056Z.1ba350c30d7e8f4d.afde14c882c923e492cdad8c49674fb244d84f51",
"lang":"de-en"}

f = open("model_epoch_15_gs_73590","r")
g = open("results_got","w")
#h = open("results_expexted","w") 

for line in f:
	#print (line)
	tokens = line.split(" ")
	line2 = ""
	#print(tokens)
	try:
		if(tokens[1]=='source:'):
			#print(line)
			for i in tokens[2:]:
				line2 = line2+i+" "
			print(line2)
			r = requests.get(url = url, params = data)
			data['text']=line2
			data1 = r.json()
			g.write(str(data1['text'][0]))
			print(str(data1['text'][0]))
	except:
			print("Skip")