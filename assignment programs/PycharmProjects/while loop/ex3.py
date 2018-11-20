num=int(input('enter number:'))
r = num % 10
num = num // 10
while num!=0:

    r1=num%10
    num=num//10
print(r+r1)