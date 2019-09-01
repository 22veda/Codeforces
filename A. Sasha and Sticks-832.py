#Veda Kailasam
n,k=map(int,input().split())
ans=n//k
if(ans&1):
    print('YES')
else:
    print('NO')