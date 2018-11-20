l=[1,2,3,4]
print(list(map((lambda n:n*2),l)))
print('--------------------------')

l1=[2,4,6,8]
l2=[2,2,2,2]
print(list(map((lambda n1,n2:n1*n2),l1,l2)))

