class A:
    def __init__(self,idno):
        self.idno=idno
class B(A):
    def __init__(self,idno,name):
        super().__init__(idno)
        self.name=name
    def display(self):
        print(self.idno)
        print(self.name)
b=B(100,'madhu')
b.display()