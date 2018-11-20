class A:
    def __init__(self):
        print('class A default constructer')
class B(A):
    def __init__(self):
        super().__init__()
        print('class B default constructer')
b=B()