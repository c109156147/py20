list1=list(input("輸入值為:"))
list1.sort()
b=sorted(list1,reverse=True)
str1=int('%s'*len(list1) % tuple(list1))
str2=int('%s'*len(b) % tuple(b))
t=str2-str1
print("最大數值列嶼最小數值列差值為:"+str(t))


