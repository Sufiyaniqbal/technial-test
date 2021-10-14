str1=input("enter a string:");
substr=input("enter a substring:");
if str1.islower():
	if substr.islower():
		count=str1.count(substr);
		print count;
	else:
		lsubstr=substr.lower();
		count=str1.count(lsubstr);
		print count;
else:
	lstr1=str1.lower();
	count=lstr1.count(substr);
	print count;
