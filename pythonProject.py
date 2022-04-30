print("Enter:")
print("Ex: 3 + 2")
a = (int)(input())
belgi = (str)(input())
b = (int)(input())
if(belgi == "+"):
		count = a + b
if(belgi == "-"):
		count = a - b
if(belgi == "*"):
		count = a * b
if(belgi == "/"):
		count = a / b
while(True):
	print("Sum:"+(str)(count))
	belgi = (str)(input())
	if(belgi == "="):
		break;
	b = (int)(input())
	if(belgi == "+"):
		count = count + b
	if(belgi == "-"):
		count = count - b
	if(belgi == "*"):
		count = count * b
	if(belgi == "/"):
		count = count / b
	
print(count)
 