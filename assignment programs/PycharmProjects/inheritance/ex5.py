class A:
    def __init__(self,idno):
        print('class A default constructer')
        self.idno=idno

class B(A):
    def __init__(self,idno,name):
        super().__init__(idno)
        self.name=name
        print(self.idno)
        print(self.name)
        print('class B default constructer')
b=B(50,'madhu')
