class A:
    def __init__(self):
        print('asdf')
class B(A):
    def __del__(self):
        print('deleted')
    def show(self):
        print('mnbvc')

b=B()
b.show()