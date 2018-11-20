n1=int(input('enter n1:'))
n2=int(input('enter n2:'))
n3=int(input('enter n3:'))
if (n1>n2) and (n1>n3):
    print(n1, 'is big')

elif (n2 > n3) and (n2 > n1):
    print(n2,'is big')
else:print(n3, 'is big')
