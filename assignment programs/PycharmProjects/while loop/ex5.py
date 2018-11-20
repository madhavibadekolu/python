class first:
    def calc(self,no1,no2):
        print('sum=',no1+no2)
        print('sub=',no1-no2)
class second(first):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print('mul=',no1*no2)
        print('div=',no1/no2)
class third(second):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print('square=',no1**2)
        print('mod=',no1%no2)
t=third()
t.calc(10,2)


