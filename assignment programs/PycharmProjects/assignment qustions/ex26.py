positive=0
negative=0
for i in range(1,11):
    num=int(input('enter number:'))
    if num>=0:
        positive+=1
    else:
        negative+=1
print('positive numbers are=',positive)
print('negative numbers are=',negative)