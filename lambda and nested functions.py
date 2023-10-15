def hello():
    x = 'Mori'

    def add_nums(y, z):
        sum_num = y+z
        return sum_num
    print(add_nums(2, 3))

    # Lambda function
    # func = lambda y, z: y+z
    # print(func(2, 3))

    return 'Hello, ' + x + '!'


print(hello())