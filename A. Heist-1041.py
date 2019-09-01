#Veda Kailasam
n=int(input())
a=sorted(list(map(int, input().split())))
c=0
for i in range(len(a) - 1):
    if (a[i + 1] - a[i] > 1):
        c+=a[i + 1] - a[i] - 1
print(c)
