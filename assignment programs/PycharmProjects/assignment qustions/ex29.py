n=int(input('enter number:'))
reverse=0
while n!=0:
    remainder=n%10
    n=n//10
    reverse=(reverse*10)+remainder
print(reverse)

