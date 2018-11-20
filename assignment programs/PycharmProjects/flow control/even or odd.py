n=int(input('enter number:'))
if n<0:
    print('plz reenter positive integer')
    n = int(input('reenter number:'))
    if n%2==0:
    print(n,'is even')
else:print(n,'is odd')