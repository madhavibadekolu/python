hour_parameter=int(input('enter hour_parameter:'))
for hour_parameter in range(0,24):
    if hour_parameter<7 or hour_parameter>20:
        print('parrot is in trouble')
        break
else:print('parrot not in trouble')
