from flask import Flask   #导入FLask类
from flask import render_template   #导入render_template，叫渲染模板，帮助把想要的渲染文件给展示出来
from flask import request  #导入request
import datetime  #引入日期时间包
import sqlite3   #引入sllite3数据库

from util.handle_excel.make_file import CreateExcelFile
from util.handle_excel.static_list import StaticList

#Flask类接收一个参数__name__
app = Flask(__name__)   #初始化了一个对象，叫app

class GeTDataFromExcel:
    def __init__(self,file_name,sheet_id):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.cef = CreateExcelFile(file_name=file_name,sheet_id=sheet_id)
        self.cef.run_create()
        self.read_data = self.get_read_data()



    def get_read_data(self):
        file_name = self.file_name
        sheet_id = self.sheet_id

        test_project = "M项目专用终端定制测试bug"
        test_module = "分组数据加密通信"
        from util.handle_excel.create_return_exceldata import ReadData
        readdata = ReadData(file_name=file_name,sheet_id=sheet_id,test_project=test_project,test_module=test_module)  #实例化
        return readdata



    def get_title(self):
        readdata = self.read_data
        title_list = readdata.getTitle()
        return title_list

    def get_data_from_excel(self,lie_num):
        readdata = self.read_data

        data_list_all = readdata.readData()

        pre_list = data_list_all[int(lie_num)]
        sl = StaticList()
        mubiao_list_all = sl.QuCHongAndStaticNum(pre_list=pre_list)
        return  mubiao_list_all





#首页
@app.route('/')
def index():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/myindex.html')

#login
@app.route('/login')
def login():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mylogin.html')

#contact
@app.route('/contact')
def contact():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mycontact.html')

#gallery-video-boxed
@app.route('/gallery_video_boxed')
def gallery_video_boxed():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mygallery-video-boxed.html')

#single-page
@app.route('/single_page')
def single_page():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mysingle-page.html')

#single-page-with-img
@app.route('/single_page_with_img')
def single_page_with_img():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mysingle-page-with-img.html')

#single-video
@app.route('/single_video')
def single_video():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return render_template('moban2023/mysingle-video.html')



#统计
@app.route('/<int:numid>')
def static_base(numid):  #函数的名字可以随便起，只要符合python函数的命名规则就行
    return render_template('moban2023/index.html',
                           # scorelist=score_list,
                           # numlist=num_list,
                           # titlename = title_name,
                           # pre_name_list = pre_name_list,
                           # image_file_list = image_file_list,
                           )


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

