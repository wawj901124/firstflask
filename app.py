from flask import Flask   #导入FLask类
from flask import render_template   #导入render_template，叫渲染模板，帮助把想要的渲染文件给展示出来
import datetime  #引入日期时间包

#Flask类接收一个参数__name__
app = Flask(__name__)   #初始化了一个对象，叫app


#装饰器的作用是将路由映射到视图函数hello_world
#路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def hello_world():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return '您好呀! 欢迎欢迎，来呀'

@app.route('/index')
def index():
    return '您好'

#带参数的路由 （字符串参数）
#通过访问路径，获取用户的字符串参数
@app.route('/user/<name>')   #使用尖角号传递参数name1
def welcome(name):   #函数中的name和尖括号里的name名字一定要一致才行，才能识别
    return '您好,%s'%name+'切换'

#带参数路由  （非字符串）
#通过访问路径，获取用户的整形参数
#路径相同，但是可以根据参数类型，自动识别路由
#函数名不能一样，路径可以一样
@app.route('/user/<int:id>')   #传递一个整型（int）数据,int:id表示把传入的id参数作为一个整型数据来看
def welcome2(id):
    return '您好,%d' % id+'号的会员'

#float类型参数
@app.route('/user/<float:floatparam>')   #传递一个整型（int）数据,int:id表示把传入的id参数作为一个整型数据来看
def welcome3(floatparam):
    return '您好,%f' % floatparam+'钱'

#路由路径不能重复，用户通过唯一路径访问特定的函数
#参数类型不一样，也算是不同路径


#使用render_template展示内容
#返回给用户渲染后的网页文件
@app.route('/indextwo')
def index2():
    return render_template('indextwo.html')  #返回一个渲染模板，帮你检查这个indextwo.html文件中有没有jinja2可以识别的符号，有就将其转为html文件


#动态展示网页，向页面传递一些变量
@app.route('/indexthree')
def index3():
    mytime = datetime.date.today()  #今天的日期  #普通变量
    name_list = ['小明','小白','小黄']    #列表类型变量
    task_dict ={'任务':'打扫卫生','时间':'3小时'}    #字典类型变量
    return render_template('indexthree.html',
                           var=mytime,#变量var，变量值为mytime,var在页面用
                           namelist = name_list,  #变量namelist，值为name_list的内容
                           taskdict = task_dict, #变量taskdict,值为tast_dict
                           )

#如何进行表单提交



#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run()   #调用run方法，启动服务器
                #服务器默认没有开启debug模式,即做了修改之后，不会实时更新，需要关闭服务器重启才能生效
    # app.run(debug=True)    #开启调试模式，但是不一定有效，因为在不同的开发环境中，有的有效，有的没有效