n=5
for x in range(1,6):
    for y in range(x):
        if (x ==4 and y == 2):
            n=40
            print(n)

        else:

            print(n,end=' ')
            n = n + 5

    print()
