class Employee:
    def __init__(self):
        print('object created')
    def show(self):
        print('iam show')
    def __del__(self):
        print('object deleated')

#unreffered object
Employee().show()

#creating object(reffered object)
e=Employee()
e.show()
