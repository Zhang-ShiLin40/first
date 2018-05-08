from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    return 'hello %s' %name

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)