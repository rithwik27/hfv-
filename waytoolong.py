a=int(input())
for i in range (0,a):
    x=input()
    if len(x)>10:
        print(str(x[0])+str((len(x)-2))+str(x[len(x)-1]))
    else:
        print(x)
        
