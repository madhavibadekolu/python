class NameException(Exception):
    def __del__(self,sorry):
        super().__init__()
        return 'valid name'
    def checkname(name):
        if len(name)>=5:
            return 'valid name'
        else: raise NameException('invalid name')
    try:
        name=input('enter name:')
        res=checkname(name)
        print(res)
    except NameException as ne:
        print(ne)


