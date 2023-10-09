import re
str = input("enter string :")
reg = r'^[a-z]$|^([a-z]).*\1$'
if (re.search(reg, str)):
    print("yes")
else:
    print("no")
