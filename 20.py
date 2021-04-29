num=["123","456"]
name=["Tom","Cat"]
obj=["DTGD","CSIE"]
n=input("為:")
b=num.index(n)
a=num[b]
if n==a:
    print(str(num[b]+" "+name[b]+" "+obj[b]))
else:
    print("查無此號碼")
