try:
    n1=int(input('enter 1st number:'))
    n2=int(input('enter 2nd number:'))
    print('sum=',n1+n2)
    try:
        print('div=',n1/n2)
        print('mul=',n1*n2)
        print('sub=',n1-n2)
    except ZeroDivisionError as ze:
        print(ze)
        print('mul=', n1 * n2)
        print('sub=', n1 - n2)

except ValueError as ve:
    print('invalid input')