wd=input('enter weekday:')
vac=input('enter vacation:')
def sleep_in(wd,vac):
    if vac=='true' and (wd=='true' or wd=='false'):
        return True
    else:
        return False
res=sleep_in(wd,vac)
print(res)