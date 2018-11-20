n=1
for x in range(1,5):
    for x in range(x):
        print(n,end=' ')
        n=n+1
        if n==10:n=0
    print()


n=9
for x in range(4,0,-1):
    for y in range(x):
        print(n,end=' ')
        n=n-1
    print()

