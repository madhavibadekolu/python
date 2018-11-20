even=0
odd=0

for i in range(1,11):
    num=int(input('enter numbers:'))
    if num%2==0:
        even+=1
    else:odd+=1
print('even numbers are=',even)
print('odd numbers are',odd)

