#!:is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。id()显示内存地址。

a=[1,2,3,4]
b=a
print(a==b)
print(a is b)
print(id(a))
print(id(b))


a=[1,2,3,4]
b=a[:]
print(a==b)
print(a is b)
print(id(a))
print(id(b))
