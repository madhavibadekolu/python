balance=45000
print('Welcome to Andra bank ATM')
pin=input('Enter pin number:')
if pin ==2468:
    print('continue the process')
    amount=int(input('Enter amount:'))
    if (amount%100)==0:
        if amount<=20000:
            if amount<=balance:
                balance=balance-amount
                print('withdraw is done')
                print('available balance is=',balance)
            else:print('no balance')
        else:print('max amount is 20000 only')
    else:print('Enter amount multiplies of 100')
else:print('Enter valid pin number')
print('thanks for using ATM')
