#Veda Kailasam
#Date:2nd September,2019
n=int(input())
a=sorted(list(map(int,input().split())))
c=0
for i in range(0,len(a)-1,2):
    if(a[i]!=a[i+1]):
        if(abs(a[i]-a[i+1])>0):
            c+=abs(a[i]-a[i+1])
print(c)