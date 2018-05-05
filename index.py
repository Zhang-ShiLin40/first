#encoding: utf-8
from flask import Flask,url_for
from flask_script import Manager

import config

app = Flask(__name__)
app.config.from_object(config) # 这样也可以配置成DEBUG模式

@app.route('/')
def hello_world():
    print url_for('my_list')
    return 'Hello World!'

@app.route('/aaa/')
def my_list():
    return 'aaa'

if __name__ == '__main__':
# 运行本项目，host=0.0.0.0可以让其他电脑也能访问到该网站，port指定访问的端口。默认的host是127.0.0.1，port为5000
    app.run(host='0.0.0.0',port=9002)

