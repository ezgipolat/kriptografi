import hashlib
a=open("kripto.txt")
x=a.read()
a.close()
y=""
n=int(input("kac basamakli bir sayı uretmek istersin? "))
for i in range(0,n):
	x=hashlib.md5(x.encode('utf-8')).hexdigest()
	y=y+x[7]
print("hexadecimal hali budur: ",y)
print("decimal hali budur: ",int(y,16))
