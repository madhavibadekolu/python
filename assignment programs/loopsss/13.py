n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
def sum_double(n1,n2):
    if n1==n2:
        sum=n1+n2
        return 2*sum
    else:
        sum=n1+n2
        return sum



res=sum_double(n1,n2)
print(res)


