#Veda Kailasam
arr=[]
for _ in range(int(input())):
    s=input()
    arr.append(s)
if(len(arr)==1):
    print(arr[0])
else:
    a=[]
    maxim=1
    for i in range(len(arr)):
        a.append(arr.count(arr[i]))
    for i in range(len(arr)):
        if(arr.count(arr[i])==max(a)):
            print(arr[i])
            break