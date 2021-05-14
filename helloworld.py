from __future__ import print_function
import numpy as np
#import cv2 as cv
import matplotlib
#import tensorflow as tf
import os
import random
#from skimage import io
#from skimage import filters
# from matplotlib import pyplot as plt


def main():
    #数组，可修改,list
    L = ['Adam', 'Lisa', 'Bart']
    #const,t = ('Adam',),tuple，类似于C语言的const，固定元素
    T = ('Adam', 'Lisa', 'Bart',0,1,2,3,4,5,6,7,8,9)
    #dict ，C语言的结构体,第一个特点是查找速度快;第二个特点就是存储的key-value序对是没有顺序的！,第三个特点是作为 key 的元素必须不可变.目的是建立一一对应的关系
    d = {
        
        'Adam': 95,
        'Lisa': 85,
        'Bart': 59,
        'Paul': 75,
    }
    #有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
    #weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    ##s = set(['Adam','Lisa','Bart','Paul'])
    s = set(['A','B','C'])
    
    
    
    print('hello,world.')
    print('hello, python.')
    print('hello,','python.')
    
    a = 123		#a是一个整数
    print (a)	#这是打印变量a
    print ('a')	#这是打印字符'a'
    a = 'imooc'	#a是一个字符串
    print (a)
    
    
    x1 = 1
    d = 3
    n = 100
    x100 = np.arange(1,300,3)			#调用np.range函数，生成等差数组
    s = np.sum(x100)				#调用np.sum函数，求x100数组的和
    print (s) 
    
    
    s = 'Python was started in 1989 by "Guido".'
    print (s)
    s = 'Python is free and easy to learn.'
    print (s)
    
    #多行字符串的表达方式
    s='''Line 1
    Line 2
    Line 3
    Line 4'''
    print(s)
    
    s='Line 1\nLine 2\nLine 3\n'
    print(s)
    #raw字符串：r'this is python3'
    #raw字符串：r'''Python is created by "Guido".It is free and easy to learn.Let's start learn Python in imooc!'''
    
    print (r'''"To be, or not to be": that is the question.
    Whether it's nobler in the mind to suffer.''')
    
    print('中文')						#python2在unicode之前，所以不兼容中文，需要在'中文'之前加u表示，即print(u'中文').而python3不需要，可以直接兼容
    print ('''静夜思
    
    床前明月光，
    疑是地上霜。
    举头望明月，
    低头思故乡。''')
    
    print (2.5 + 10 / 4)
    
    a = 'python'
    print ('hello,', a or 'world')
    
    b = ''
    print ('hello,', b or 'world')
    
    
    L = [95.5, 85, 59]
    print (L[-1])						#倒数第一名
    print (L[-2])
    print (L[-3])
    print (L[0],L[1],L[2])					#正数第一，二，三名
    
    L.append('Paul')					#在L的尾部添加元素
    L.insert(2, 'Gim')					#在L的第二个位置插入元素
    print(L)
    L.pop(2)						#删除第二个元素,L.pop()为删除最后一个元素
    print(L)
    L[0] = 'Bart'
    L[-1] = 'Adam'
    print(L)
    
    score = 76
    score = 85
    
    #if用法
    if score>=90:
        print ('excellent')
    elif score>=80:
        print ('good')
    elif score>=60:
        print ('passed')
    else:
        print ('failed')
    
    #for循环用法，n就代表了新定义的变量，是L中的元素，相当于n=L[0],n=L[1]
    L = [75, 92, 59, 68]
    sum = 0.0
    for n in L:
        sum = sum + n
    print (sum / 4)
    
    #while 循环
    sum = 0
    x = 1
    while x < 100:
        sum = x + sum
        x = x + 2
    print (sum)
    #while break 循环用法
    sum = 0
    x = 1
    n = 1
    while True:
        sum = sum +x
        x = x*2
        n = n + 1
        if n > 20:
            break
    print (sum)
    #continue用法，在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。包括for循环，while循环
    sum = 0
    x = 0
    while True:
        x = x + 1
        if x > 100:
            break
        if x % 2 ==0:
            continue
        sum = sum + x
    print (sum)
    #对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
    '''
    for x in range(1,10):
        for y in range(0,10):
            if x<y:
               print(x*10+y)
    '''
    
    #打印dict的元素
    d = {
        'Adam': 95,
        'Lisa': 85,
        'Bart': 59
    }
    print ('Adam:',d['Adam'])
    print ('Lisa:',d['Lisa'])
    print ('Bart:',d['Bart'])
    
    
    d = {
        95: 'Adam',
        85: 'Lisa',
        59: 'Bart'
    }
    d[72] = 'Paul'
    print(d)
    for n in d:
        print (n,':',d[n])
    
    #月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。
    months = set(['Jan','Feb','Mar','Apr'])
    x1 = 'Feb'
    x2 = 'Sun'
    
    if x1 in months:
        print ('x1: ok')
    else:
        print ('x1: error')
    
    if x2 in months:
        print ('x2: ok')
    else:
        print ('x2: error')
    
    #针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
    s = set(['Adam', 'Lisa', 'Paul'])
    L = ['Adam', 'Lisa', 'Bart', 'Paul']
    for x in range(4):
        if L[x] in s:
            s.remove(L[x])
        else:
            s.add(L[x])
    print (s)


main()

















