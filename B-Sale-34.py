#Veda Kailasam
n,m=map(int,input().split())
p=sorted(list(map(int,input().split())))
a=[]
for i in range(len(p)):
    if(i<m and p[i]<0):
        a.append(p[i])
print(abs(sum(a)))