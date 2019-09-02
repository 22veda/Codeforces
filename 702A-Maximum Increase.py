#Veda Kailasam
#Date:2nd September,2019
n=int(input())
a=list(map(int,input().split()))
c,maxim=1,1
for i in range(len(a)-1):
    if(a[i]<a[i+1]):
        c+=1
        if(c>maxim):
            maxim=c
    else:
        if(c>maxim):
            maxim=c
        c=1
if(c>maxim):
    maxim=c
print(maxim)