from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    user_agent=request.headers.get('User_Agent')
    return "user agent is %s"%user_agent

@app.route('/<name>')
def user(name):
    return 'hello %s' %name

if __name__=='__main__':
    app.run()
