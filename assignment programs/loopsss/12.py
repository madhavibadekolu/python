a_smile=input('enter a :')
b_smile=input('enter b:')
def monkey_trouble(a_smile,b_smile):
    if a_smile=='true' and b_smile=='true':
        return True
    elif a_smile=='false' and b_smile=='false':
        return True
    else:
        return False
res=monkey_trouble(a_smile,b_smile)
print(res)

