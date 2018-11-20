n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
bignum=lambda n1,n2:n1 if n1>n2 else n2 if n2>n1 else print('both are same')
print(bignum(n1,n2))