#!/usr/bin/env Python3
#-*- coding utf-8 -*-

'a test module'
from pip._vendor.distlib._backport.tarfile import TUREAD
'''
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
'''
'''
class Student():
    def __init__(self, name):
        self.name = name
    
    def read(self):
        print('read %s' % self.name)
        return 0
    stunum = 2

a = Student('huowu')
if hasattr(a, 'read'):
    a.read()

class Senior(Student):
    __slots__=('high', 'weight')#多用于内存优化工具，副作用是作为封装工具，防止用户给实例增加新的属性。
s2 = Senior('xiaohua')
s2.age = 28
from types import MethodType
def my_print(self):
print(s2.age)
'''
'''    
setattr(Student, 'write', lambda self, s: print(s))
print(type(getattr(Student, 'write')))
print(type(Student.write(None, 'Student')))
print(getattr(Student, "stunum"))
print(type(a.read()))
Student('None').write('nihao')
def calllist(s):
    list(filter(lambda x : hasattr(getattr(s,x), '__call__') ,dir(s)))
'''
'''
Student.write(None, 'huowu')
a.write('a')

print(type(Student))
b = Student('b')
b.write('b')
''' 
'''
class Student(object):
    def __init__(self, birth = 2017):
        self._birth = birth
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student(1988)
s.birth = 1977
print(s.birth)
print(s.age)
'''
'''
class Screen(object):
    def __init__(self, width = 800, height = 600):
        self._width = width
        self._height = height
    #width
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, wide):
        self._width = wide
    
    #height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, high):
        self._height = high
    
    #resolution
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024#把s._width封装起来
s.height = 768
print(s.resolution)
'''
'''
class A(object):
    def put_out(self):
        return 'A'
    def print_outa(self):
        return 'a'

class B(object):
    def put_out(self):
        return 'B'

class C(A,B):
    pass

class D(B,A):
    pass

class E(D):#不能同时继承A与D-->TypeError: Cannot create a consistent method resolution order (MRO) for bases A, D
    def put_out(self):
        return 'E'
    def print_out(self):
        return 'e'

X=C()
print(X.put_out())
Y=D()
print(Y.put_out())
M=E()
print(M.put_out(),M.print_out(),M.print_outa())
'''
'''
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, member, '=', member.value)
print(type(Month.__members__.items()))
print(Month.Jan.value, Month.Jan.name)    
print(Month.Jan, Month.Jan.name, Month.Jan.value)
print(type(Month.Jan))
print(type(Month))
for month in Month:
    print(month.value)
print(dir(Month))
'''
'''
from enum import Enum
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6
print('weekday type = %s' %(type(Weekday)))
print('weekday[1] type = %s' %(type(Weekday(1))))
print((Weekday(1).value))
print(Weekday)
print(type(Weekday(1).value))
def isItem(name):
    for key in Weekday:
        if key.name == name:
            return True
    return False
print(isItem('Wed'))   
'''
'''
def fn(self, name = 'world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello = fn))
h = Hello()
h.hello()
print(Hello.__metaclass__)    
'''
'''
class FlyToSky(object):
    pass
pw = type('Tick', (FlyToSky,), {'laugh_at':'hahahaha'})
print(pw().laugh_at)
print(pw.__bases__)
print(pw.__class__)
print(pw().__class__)   
print(pw().__dict__)    
'''
'''
import pdb
def foo(s):
    n = int(s)
    pdb.set_trace()
    if n==0:
        print('before raise')
        raise ValueError('invalid value: %s' % s)
    print('after raise')
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError! %s' % e)
        raise
bar()
print('after bar')
'''
'''
import os

def findwords(dir, s):
    #print([x for x in os.listdir(dir)if os.path.isdir(os.path.join(dir, x))])
    downdirs = [os.path.join(dir, x) for x in os.listdir(dir) if os.path.isdir(os.path.join(dir, x))]
    downfiles = [x for x in os.listdir(dir) if os.path.isfile(x) and s in os.path.split(x)[1]]
    if downfiles:
        print(downfiles)
    #dfindwords(downdir, s) for downdir in downdirs
    if downdirs:
        for downdir in downdirs:
            findwords(downdir, s)
 #
findwords('/home/huowu/workspace', 'py')
'''
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''
from datetime import datetime
print(datetime.now())
print(datetime.now())



    
    
    