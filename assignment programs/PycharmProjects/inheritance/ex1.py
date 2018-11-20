class A():
    def assign(self):
        print('iam class A')
class B(A):
    def show(self):
        print('iam class B')

x=B()
x.assign()
x.show()