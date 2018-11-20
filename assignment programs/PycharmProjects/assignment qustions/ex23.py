n=int(input('enter number:'))
for x in range(2,n):
    if n%x==0:
        print(n,'is not a primenumber')
        break
    else:
        print(n,'is a primenumber')
        break