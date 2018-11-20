num=int(input('enter number:'))
sum=0
while num!=0:
    remainder=num%10
    num=num//10
    sum+=remainder
print(sum)
