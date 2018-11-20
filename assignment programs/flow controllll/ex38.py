str=input('enter string:')
result=''
for x in range(len(str)):
    result+=str[:x+1]
print(result,end='')