emp_name=input('enter employee name:')
salary=int(input('enter salary:'))
designation=input('enter designation:' )
if designation=='manager':
    salary=salary+(salary*20/100)
    print('total salary',salary)
elif designation=='analyst':
    salary=salary+(salary*10/100)
    print('total salary',salary)
elif designation=='clerk':
    salary=salary+(salary*5/100)
    print('total salary',salary)
else:print('enter valid designation')