total_marks=int(input('enter number:'))
if total_marks>360:
    print('first class')
elif total_marks<360 and  total_marks>=300:
    print('second class')
else:
    print('third class')