#Veda Kailasam
#Date:2nd September,2019
n=int(input())
a = n % 4
if(n==0):
    print("1")
elif(a==1):
    print('8')
elif(a==2):
    print('4')
elif(a==3):
    print('2')
elif(a==4 or a==0):
    print('6')