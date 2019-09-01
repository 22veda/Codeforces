#Veda Kailasam
n=int(input())
a=input()
c=0
for i in range(len(a)-2):
    if(a[i]=='x' and a[i+1]=='x' and a[i+2]=='x'):
        c+=1
print(c)
