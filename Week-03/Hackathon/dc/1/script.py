str1 = ""

for row in range(7):
	for col in range(5):
		if ((clo==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
			str1 = str+"*"
		else: 
			str1 = str+" "
	

print(str)