m=int(input("請輸入一個度數:"))
if(m<121):
    s=m*2.1
    w=m*2.1
    print("Summer months:"+str(s))
    print("Non-Summer months:"+str(w))
elif(m>120 and m<331):
    s=120*2.1+((m-120)*3.02)
    w=120*2.1+((m-120)*2.68)
    print("Summer months:"+str(s))
    print("Non-Summer months:"+str(w))
elif(m>330 and m<501):
    s=120*2.1+210*3.02+((m-330)*4.39)
    w=120*2.1+210*2.68+((m-330)*3.61)
    print("Summer months:"+str(s))
    print("Non-Summer months:"+str(w))
elif(m>500 and m<701):
    s=120*2.1+210*3.02+170*4.39+((m-500)*4.97)
    w=120*2.1+210*2.68+170*3.61+((m-500)*4.01)
    print("Summer months:"+str(s))
    print("Non-Summer months:"+str(w))
else:
    s=120*2.1+210*3.02+170*4.39+200*4.97+((m-700)*5.63)
    w=120*2.1+210*2.68+170*3.61+200*4.01+((m-700)*4.5)
    print("Summer months:"+str(s))
    print("Non-Summer months:"+str(w))

