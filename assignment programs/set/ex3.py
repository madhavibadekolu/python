s1={1,2,4}
s2={1,5,6}
s3=s1.issuperset(s2)
print(s3)

print('-------------')
s1.pop()
print(s1)

s1={1,2,3}

s1.remove(3)
print(s1)



s1={1,2,4}

s2={1,2,6}

s6=s1.union(s2)
print(s6)
s1.update({4,6,7})
print(s1)