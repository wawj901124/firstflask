from flask import Flask   #导入FLask类
from flask import render_template   #导入render_template，叫渲染模板，帮助把想要的渲染文件给展示出来
from flask import request  #导入request
import datetime  #引入日期时间包
import sqlite3   #引入sllite3数据库

#Flask类接收一个参数__name__
app = Flask(__name__)   #初始化了一个对象，叫app


#装饰器的作用是将路由映射到视图函数hello_world
#路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def index():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('index.html')

#首页
@app.route('/index')
def home():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    # return render_template('index.html')
    return index()   #或者直接返回一个函数

#电影
@app.route('/movie')
def movie():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    movie_list = []
    # con = sqlite3.connect('movie.db')  #连接数据库
    # cur = con.cursor()  #游标
    # sql = 'select * from movie250'  #数据库查询语句
    # data = cur.execute(sql=sql)  #执行查询语句，得出查询后的结果
    # for item in data:
    #     movie_list.append(item)   #如果不保存在本地变量中，查询出的数据会随着游标关闭和数据库连接关闭而消失，无法访问
    # cur.close()  #关闭游标
    # con.close()  #关闭数据库连接

    #此处没有数据库，用固定数据代替
    data = [
        ['1','https://movie.douban.com/subject/1292052/','0','肖申克的救赎','The Shawshank ReDemption','9.7','1895120','希望让人自由','导演：弗兰克...'],
        ['2', 'https://movie.douban.com/subject/1291546/', '0', '霸王别姬', '','9.6', '1390500', '风华绝代', '导演：陈凯歌...'],
        ['3', 'https://movie.douban.com/subject/1292720/', '0', '阿甘正传', 'Forrest Gump','9.5', '1442700', '一部美国近现代史', '导演：罗伯特...'],
    ]
    for item in data:
        movie_list.append(item)


    return render_template('movie.html',
                           movies=movie_list,   #将movie_list放到movies变量中，供网页访问
                           )

#评分
@app.route('/score')
def score():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('score.html')


#词云
@app.route('/word')
def word():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('word.html')


#词云
@app.route('/team')
def team():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('team.html')




#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run()   #调用run方法，启动服务器
                #服务器默认没有开启debug模式,即做了修改之后，不会实时更新，需要关闭服务器重启才能生效
    # app.run(debug=True)    #开启调试模式，但是不一定有效，因为在不同的开发环境中，有的有效，有的没有效
    #flask默认开启的网站是本地的：127.0.0.1:5000
    #现在把已经有的本机访问改成局域网
    #host='0.0.0.0'，配置host为0.0.0.0
    #port = 8080,配置端口
    #访问服务器的ip地址即可
    # app.run(host='0.0.0.0',port = 8080)

