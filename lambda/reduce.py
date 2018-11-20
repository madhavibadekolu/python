from functools import reduce
l=[1,2,3,4]
print(reduce((lambda n,m:n+m),l))
