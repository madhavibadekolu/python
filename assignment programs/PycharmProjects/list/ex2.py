marks=[56,26,74,12,45,30]
print('total marks=',sum(marks))
print('highest marks=',max(marks))
print('lowghest marks=',min(marks))
print('average=',sum(marks)/len(marks))
for x in range(len(marks)):
    if  marks[x] >=35:
        print('subject', x+1 ,'is pass')
    else:
        print('subject',x+1,'is fail')
