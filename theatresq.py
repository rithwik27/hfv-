x=list(map(int, input().split()))
if x[0]%x[2]==0:
    count=0
else:
    count=1
sum2=x[0]//x[2]+count
if: x[1]%x[2]==0:
    count=0
else:
    count=1
sum1=x[0]//x[2]+count
flag=sum1*sum2
print flag
