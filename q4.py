import re
f = open("C:/Users/Saurabh Raj/Desktop/python/lab-9/inputmail.txt", 'r')
f1 = open("C:/Users/Saurabh Raj/Desktop/python/lab-9/validmail.txt", 'w')
\
lst = f.readlines()

lst = f.readlines()
pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
for line in lst:
    if re.match(pat, line):
        f1.write(line)
        print(line)


f.close()
f1.close()
