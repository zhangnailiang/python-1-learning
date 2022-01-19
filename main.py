print("ddd"),
#这是个单行注释
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
print(1+1),
print(2-1),
print(3*4),
print(8//4),
print(3%4),
#整除
#取余
print(2**4),
print(2>1),
print(3==4),
print(3!=4),
print((3>2) and (3<5)),
#非
print(not (2<1)),
print(not((3>2) and (3<5))),
#位运算符
print(bin(4)),
print((bin(5))),
print(bin(5<<2)),
print(bin(5>>2)),
#三元运算符
x,y = 4,5
if x > y:
   small = x
else:
   small = y
print(small)
#三元替代者
x,y = 4,5
small = x if x < y else y
print(small)
#其他操作符
'''
in not in  is  not is
'''
#eg:
letters = ["a","b","c"]
if "a" in letters:
    print("a"+" exists")
if "h" not in letters:
    print("h"+"not exissasdts")
#其余的运算符
print(1/9),
print('ascasc')
##身份运算符 is is not not 
a = 'hello'
b = 'hello'
print(a is b, a == b),
#地址是一样的  is比较的是  地址  == !=对比的是相同的值
#变量和赋值
#使用变量前需要对其先赋值
#变量名可以包括字母、数字、下划线，但不能以数字未开头
#大小写是敏感的

teacher = '老妈的程序人生'
print(teacher)
first = 2
second = 3
third = first + second
print(third)

myTeacher = '老妈的程序人生'
yourTeacher = '小马的程序人生'
ourTeacher = myTeacher + yourTeacher
print(ourTeacher)

set_1 = ["欢迎", "学习","Python"]
print(set_1.pop())

a = 1031
print(a, type(a))
# 1031 <class 'int'>
#python中万物皆对象 zhengxiing  还有相应的属性和方法
#int float bool  整形  浮点型  布尔型

b = dir(float)
print(b)

#找到一个整数的二进制表示，再返回其长度

a = 5
print(bin(a))
print(a.bit_length())
#浮点型数字
print(1,type(1)),
print(1.8)


a = 0.00023
b = 2.3e-5
print(b)
import decimal
from decimal import Decimal, getcontext
from imp import init_builtin
from traceback import print_list

a = decimal.getcontext()
print(a),
print(1, type(1)),
print (1, type(1)),


#两种python package的引入方式
'''
import 和 from decimal import Decimal/*
'''
import decimal
a = decimal.getcontext(),
print(a)

#dir 返回对象的属性列表

print(dir(decimal)),

b = Decimal(1)/Decimal(3)
print(b)


decimal.getcontext().prec = 7
c = Decimal(1) / Decimal(3)
print(getcontext())

#布尔型 布尔型在数字运算中  1表示的是true  表示的0
'''
布尔型变量只能去两个值  true and false  当吧布尔型变量用在数字与  用 1和0代表trueand false
'''
print(True + 0),


print(type(0)),
print(type(10.31),bool(0.00), bool(10.31)),

print()


'''
bool 作用在容器类型变量: 字符串  元祖  列表  字典和集合

元祖和列表相似 但是元祖使用()使用小括号  列表 使用方括号   元祖内容不能更改
  列表内容可以修改
  元组创建

  列表也是集合，是特殊的集合，有序，可重复，用序号调用
  集合就是一个最小的类型单位，无序、内容不能重复，通过set的方法创建

'''

print(type(''), bool(''), bool('python'))


print(type(()), bool(()), bool(10,))
print(type([]), bool([]), bool([1,2]))


print(type({}), bool({}), bool({"a":1, 'b':2}))

print(type(set()), bool(set()), bool(set({"a":1, 'b':2})))


bool(x)
#true还是false 就看x是不是空的，空的话就是false，不空的就是true


#bool作为数值变量  ，0和0.00都是认为是空的
#对于容器变量，里面没元素就是空的


#获取类型信息type（object)
print(isinstance(1,int ))
print(isinstance(5.3, float))
print(isinstance(True, bool)),
print(isinstance('5.2',str))

print()


if 2 > 1 and not 2 > 3:
    print("sdf")
print("dfsf")


# temp = input("猜一猜小姐姐想的是哪个数字？")
# guess = str(temp) # input 函数将接收的任何数据类型都默认为 str。

# if guess == "666":
#     print("guess"+guess)
#     print("你太了解小姐姐的心思了！")
#     print("哼，猜对也没有奖励！")
# else:
#     print("guess"+guess)
#     print("猜错了，小姐姐现在心里想的是666！")
# print("游戏结束，不玩儿啦！")


print(isinstance(1, int))

'''
类型转换
转换为int  str   float(x)
'''

print(int("520")),
print(int(520.52))
print(float("520.52")),
print(float(520)),
print(str(10+10)),


#内部相加之后再  str类型转化
print(str(10.1+5.2))


shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed without 'end' and 'sep'"),
for item in shoplist:
    print(item)
