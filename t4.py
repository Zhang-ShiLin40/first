from main import app
from flask import current_app
from flask import g
#参考：https://blog.csdn.net/hyman_c/article/details/52556562
#flask全局变量
ctx=app.app_context()
ctx.push()
#1.current_app
#current_app代表当前的flask程序实例,使用时需要flask的程序上下文激活
print current_app.name
#2.g
#g作为flask程序全局的一个临时变量,充当者中间媒介的作用,
# 我们可以通过它传递一些数据,下面的例子,通过g传递了一个名字叫做"lisa",
# 使用g之前也需要激活程序上下文:
g.name='lisa'
print g.name
#3.request对象
#请求对象,封装了客户端发送的HTTP请求的内容

#4.session
# 用户会话,用来记住请求(比如前后一个GET请求和一个POST请求)之间的值,
# 从数据格式上来说它是字典类型。它存在于连接到服务器的每个客户端中，
# 属于私有存储，会保存在客户端的cookie中。