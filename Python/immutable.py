#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def ChangeInt( a ):
    a = 10
    print (a)

b = 2
ChangeInt(b)
print (b) # 结果是 2实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它
'''不可变类型immutable：类似 c++ 的值传递，
   如 整数、字符串、元组。如fun（a），
   传递的只是a的值，没有影响a对象本身。
   比如在 fun（a）内部修改 a 的值，
   只是修改另一个复制的对象，
   不会影响 a 本身。'''
# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print ("函数内取值: ", mylist)
    return
             
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)

"""实例中传入函数的和在末尾添加新内容的对象用的是同一个引用，故输出结果如"""
