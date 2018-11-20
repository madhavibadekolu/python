class A:
    def m1(self):
        i=8956
        print('grfsd')
        print(i)
class B(A):
    i = 853
    def m2(self):
        print(B.i)
x=B()
x.m1()
x.m2()
