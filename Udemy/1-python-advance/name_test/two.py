import one


def fun_two():
    print('This is Fun two')


print('eeeeeeeeeeeeeeeeee')

if __name__ == '__main__':
    print(__name__)
    one.fun_one()
    fun_two()
else:
    print(__name__)
    print('This is not main')
