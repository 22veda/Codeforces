#Veda Kailasam
def sum1(n):
    s=0
    while n>0 and s<11:
        s+=(n%10)
        n=n//10
    return s 
n=int(input())
i=19
cnt=0
while 1:
    if sum1(i)==10:
        cnt+=1
    if cnt==n:
        print(i)
        break
    i+=9
