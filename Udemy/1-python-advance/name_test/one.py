def fun_one():
    print('This is Fun one')


if __name__ == '__main__':
    print(__name__)
    fun_one()
else:
    print('XXXXX')
    print(__name__)
    print('This is not main')


print('ssssssssssssssssssssssssssss')


# When you import a Python file (module), any code at the top level of that file (outside of any functions or classes) gets executed immediately.
