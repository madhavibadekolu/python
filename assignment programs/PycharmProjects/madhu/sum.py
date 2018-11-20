class Employee:
    def __init__(self,idno,name):
        self.idno=idno
        self.name=name
    def display(self):
        print(self.idno)
        print(self.name)
e1=Employee(100,'madhu')
e1.display()
print(type(e1))
e2=Employee(200,'rishi')
e2.display()
print(type(e2))
