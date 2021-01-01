from flask import Flask   #导入FLask类

#Flask类接收一个参数__name__
app = Flask(__name__)


#装饰器的作用是将路由映射到视图函数hello_world
@app.route('/')
def hello_world():
    return 'Hello World!'


#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run()
