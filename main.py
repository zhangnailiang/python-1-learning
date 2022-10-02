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
from os import sep
import string
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







shoplist = ['apple','mango','carrot','banana']
print("this is printed with ")
for item in shoplist:
    print(item,end='&')

print("/n")

#sep是多参数想要输出时 各个参数中间的  分隔符
for item in shoplist:
    print(item, "another string","znlzbsbb",sep="&"),



'''
位运算
1.原码  反码  补码
原码就是二进制表示
反码就是  分为 正数 和  负数
         正数的反码   是本身   
         负数的反码   是符号位不变  其余按位取反
补码     正数的补码就是原码  负数的补码就是原码加一

符号位就是  最高位就是符号位   0表示正数  1表示负数  其中符号位也参与运算
'''
#if语句
if 2 > 1 and not 2 > 3:
    print("Corrot judgement")


hi = 6
if hi > 2:
    if hi > 7:
        print("好棒阿尼")
    else:
        print("asdas")
else:
    print("qie  shibailele")


#if else 合并语句
# temp = input("请输入成绩:")
# source = int(temp)
# if 100 >= source >= 90:
#     print("A")
# elif 90 > source >= 80:
#     print("B")
# else:
#     print("no pass")


#assert关键词
# assert 3 > 7



# while的
count = 0
# while count < 3:
#     temp = input("猜猜小姐姐想的是哪个单词？")
#     guess = int(temp)
#     if guess > 8:
#         print("大了大了")
#     else:
#         if guess == 8:
#             print("你太了解小姐姐的心思了")
#             count = 3
#         else:
#             print("小了小了")
#     count = count + 1
# print("游戏结束，不玩了")
string = "abcd"
while string:
    print(string)
    string = string[1:]



#while-else  循环
count = 0
while count < 5:
    print("%d is less than 5" % count)
    count = count + 1
else:
    print("%d is not than 5" % count)

count = 0
while count < 5:
    print("%d is less than 5" % count)
    count = 6
    break
else:
    print("%d is less than 5" % count)

#for 循环
for i in "ILOVELSGO":
    print(i, end=" ") #不换行输出
member = ['张三', '李四', '刘德华', '刘六', '周润发']
for each in member:
    print(each)


#range 使用的是  range(stop)就是默认从第0
print("member的长度：",len(member))
print("range(len(member))是什么：",range(len(member)))
for i in range(len(member)):
    print(member[i])
x = "runoob"
for i in range(len(x)):
    print(x[i],end=" ")


dic = {"a":1, "b":2}
for key in dic.keys():
    print(key, end=" ")
for value in dic.values():
    print(value, end=" ")

member = ["张三", "李四", "刘德华", "周润发"]
for each in member:
    print(each)
for key, value in dic.items():
    print(key, value, sep=":", end=" ")

''''
for else语句 for在正常执行完的情况下，之行else中的内容  
如果for循环中 执行了跳出循环的语句  使用break
for-else and while-else  ("for-else" is similar to "while-else."）
'''
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d 等于 %d %d" % (num, i ,j))
            break
    else:
        print(num, "这是一个质数")

#the range() Function
for i in range (2,9):
    print(i)

# range() the third parameter can specify a different increment(even negative; sometimes this is called the "step")
for a in range (1, 10, 2):
    print(a)

#enumerate  (sequence(iterable), [start = 0]);
seasons = ["spring", "Summer", "fall", "winter"]
lst = list(enumerate(seasons))
print(lst)
print(enumerate(seasons, start=1))

# euqivalent use-defined function
# def enumerate1(sequence, start = 0):
#     n = start
#     for i in 


def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        print (b)
        a, b = b, a + b 
        n = n + 1
fab(5)
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b , a + b
        n = n + 1
    return L
for n in  fab(5):
    print (n)