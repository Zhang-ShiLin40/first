#!/usr/bin/env python
from time import ctime,sleep

def settime(func):
    def tempfun():
       # print "[%s]%s called"%(ctime
        print func()+"[%s]%s called"%(ctime(),func.__name__)
        return func
    return tempfun

@settime
def myfunc():
    return"aaaa"


myfunc()
sleep(4)

for i in range(3):
    myfunc()
    sleep(1)