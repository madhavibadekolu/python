fname=input('filename')
try:
    file=open(fname)
    text=file.read()
    print(text)
    file.close()
except FileNotFoundError as fnf:
    print(fnf)
else:
    print('no reading data')