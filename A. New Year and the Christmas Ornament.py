y,b,r=map(int,input().split())
for i in range(r,1,-1):
    if((i-1)<=b and (i-2)<=y):
        print((i*3)-3)
        break