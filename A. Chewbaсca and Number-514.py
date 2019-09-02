#Veda Kailasam
n=int(input())
a=[]
while (n > 0):
    x=n % 10
    a.append(str(min(x, 9 - x)))
    n=n // 10
a=a[::-1]
if (x == 9):
    a[0]='9'
print("".join(map(str, a)))
