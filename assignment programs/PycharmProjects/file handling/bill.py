cust_name=input('enter customer name:')
units=int(input('enter units:'))
a=input('enter type:')
if a=='industry':
    Bill1=units*5.25
    print('industry bill is',Bill1)
elif a == 'commercial':
    Bill2=units*4.00
    print('commercial bill is',Bill2)
elif a == 'residence':
        Bill3 = units * 3.08
        print('residence bill is', Bill3)
else:print('enter valid type')



