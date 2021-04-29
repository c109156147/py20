n=int(input(":"))
t=0
list1=[]
for i in range(1,n+1):
    t=0
    a,b=input("第"+str(i)+"組").split(" ")
    t=int(a)*250+int(b)*175
    list1.append(t)
for j in range (1,n+1):
    print("$:"+str(list1[j-1]),end="\n")
