from flask import Flask   #导入FLask类
from flask import render_template   #导入render_template，叫渲染模板，帮助把想要的渲染文件给展示出来
from flask import request  #导入request
import datetime  #引入日期时间包

#Flask类接收一个参数__name__
app = Flask(__name__)   #初始化了一个对象，叫app


#装饰器的作用是将路由映射到视图函数hello_world
#路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def hello_world():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('index.html')


#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run()   #调用run方法，启动服务器
                #服务器默认没有开启debug模式,即做了修改之后，不会实时更新，需要关闭服务器重启才能生效
    # app.run(debug=True)    #开启调试模式，但是不一定有效，因为在不同的开发环境中，有的有效，有的没有效