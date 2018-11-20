class s1:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class s2(s1):
    def show(self):
        print(self.id)
        print(self.name)
a=s2(21,'madhu')
a.show()
