M=int(input("請輸入階層值M:"))
i=1
n=1
while(n<M):
    i=i+1
    n=n*i
print("超過M為"+str(M)+"的最小階層N值為:"+str(i))
