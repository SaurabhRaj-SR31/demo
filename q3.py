f = open("C:/Users/Saurabh Raj/Desktop/python/lab-9/input.txt", 'r+')
lst = f.readlines()
lst.reverse()
f.truncate(0)
f.seek(0)

f.writelines(lst)


f.close()
