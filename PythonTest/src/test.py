"""#!/usr/bin/env python
"""
import copy
"""
from _collections import _deque_iterator

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
L3 = [s for s in L1 if isinstance(s, str)]
print(L2)
print(L3)
"""
'''
import copyreg
def triangles():
    n = 1
    lastlist = [1]
    newlist = []
    while True:
        newlist.clear()
        for i in range(n):
            if i == 0 or i == n-1:
                newlist.append(1)
            else:
                newlist.append(lastlist[i-1]+lastlist[i])
        lastlist = copy.copy(newlist)
        n += 1
        yield newlist
        
n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
'''
'''
import functools

def log(func):
    @functools.wraps(func)//作为装饰器把函数的名称修改成func
    def wrapper(*args, **wk):
        print('call %s():' % func.__name__)
        return func(*args, **wk)
    return wrapper

@log
def test():
    print('wrapper test')

now = log(test)
print('now name = %s' % now.__name__)
    
'''
'''
import functools

def log(text):
    if isinstance(text,str):
        def detector(func):
            @functools.wraps(func)
            def wrapper(*args, **wk):
                print('begin call')
                print('%s:%s' %(text, func()))
                print('end call')
            return wrapper
        return detector
    else:
        @functools.wraps(text)
        def warpper(*args, **wk):
            print('begin call')
            text()
            print('end call')            
        return warpper
@log("test")
def test():
    print("call one time")
test()
'''
'''
import functools
int2 = functools.partial(int, base = 2)
print(int2('1000', base = 10))
print(float('1.2'))
'''
'''
import mycompany
mycompany.test.test()
'''



    