#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael': 95,'Bob': 75,'Tracy': 85}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))



dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
  
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
   

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print({x: x**2 for x in (2, 4, 6)})

print(id(dict))           #id()返回内存地址

a=1
b=1
print(a is b)
print(id(a),"\n", id(b))
