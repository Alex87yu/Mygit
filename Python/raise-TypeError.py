def my_abs(x):
#e    if not isinstance(x, (int, float)):
#        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs('a'))

#不是数字不能比较，自己添加一个报错
