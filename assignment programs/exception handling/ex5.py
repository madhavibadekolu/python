def checkage(age=0):
    if age>=23:
        return 'valid age'
    else:
        raise ValueError('invalid age')
try:
    age=int(input('enter age:'))
    res=checkage(age)
    print(res)
except ValueError as ve:
    print(ve)