f = open("model_epoch_15_gs_73590","r")
g = open("results_expected","w")
for line in f:
	tokens = line.split(" ")

	try:
		line2 = ""
		if tokens[1]=="expected:":
			print(tokens)
			for i in tokens[2:]:
				line2=line2+i+" "
		print(line2)
		g.write(line2)
	except:
		pass