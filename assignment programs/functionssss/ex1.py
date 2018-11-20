def outer():
    print('iam outer function')
    def inner():
        print('iam inner')
    inner()

    def show():
        print('show')
    show()

    print('other statement')
outer()