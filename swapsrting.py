string=input("enter a string:");
newstring="";
for x in range(0,len(string)):
	if string[x].islower():
		newstring+=string[x].upper();
	elif string[x].isupper():
		newstring+=string[x].lower();
	else:
		newstring+=string[x];
print("swaping done:"+newstring);

