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

    def get_data_from_excel_two_lie(self,zhu_lie_num,fu_lie_num):
        readdata = self.read_data

        data_list_all = readdata.readData()

        zhu_list = data_list_all[int(zhu_lie_num)]
        fu_list = data_list_all[int(fu_lie_num)]

        sl = StaticList()
        mubiao_list_all = sl.handleTwoList(zhu_list=zhu_list,fu_list=fu_list)
        return  mubiao_list_all





#首页
@app.route('/')
def index():  #函数的名字可以随便起，只要符合python函数的命名规则就行\
    return static_base_three(3,0)


#统计
@app.route('/<int:zhunumid>_<int:funumid>')
def static_base_three(zhunumid,funumid):  #函数的名字可以随便起，只要符合python函数的命名规则就行
    # file_name = r"D:\pycharmproject\firstflask\importexcel\chandao\excelbiaodata\七合一 Mate30E pro -未关闭Bug.xls"
    file_name = r"D:\PycharmProjects\firstflask\util\handle_excel\exceldata\dataresult.xls"
    sheet_id = 0

    gdfe = GeTDataFromExcel(file_name=file_name,sheet_id=sheet_id)
    pre_name_list = gdfe.get_title()   #获取标题所有内容
    print("pre_name_list:")
    print(pre_name_list)
    # pre_name_list = ['Bug编号', '所属产品', '所属模块', '所属项目', '相关研发内部优化改进的需求', '相关任务', 'Bug标题', '关键词', '严重程度', '优先级', 'Bug类型', '操作系统', '浏览器', '重现步骤', 'Bug状态', '截止日期', '激活次数', '是否确认', '抄送给', '由谁创建', '创建日期', '影响版本', '指派给', '指派日期', '解决者', '解决方案', '解决版本', '解决日期', '由谁关闭', '关闭日期', '重复ID', '相关Bug', '相关用例', '最后修改者', '修改日期', '子状态', '附件']
    zhu_lie_num = int(zhunumid)
    print(zhu_lie_num)

    fu_lie_num = int(funumid)
    print(fu_lie_num)

    # title_name = pre_name_list[lie_num]
    mubiao_list_all = gdfe.get_data_from_excel_two_lie(zhu_lie_num=zhu_lie_num,fu_lie_num=fu_lie_num)

    #获取主列的标题数据
    zhu_lie_title_name = pre_name_list[zhu_lie_num]

    print("zhu_lie_title_name:")
    print(zhu_lie_title_name)
    print(" mubiao_list_all:")
    print( mubiao_list_all)
    hengzhou_name_list = mubiao_list_all[0]   #横轴标题内容
    zongzhou_name_list = mubiao_list_all[1]  #纵轴标题内容

    #计数data（即Y轴标题）: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎', '百度', '谷歌', '必应', '其他']
    #x轴data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

    # #生成source数据
    # source: [
    #     ['titte', '北京', '南京', '河北', '保定', '太原'],
    #     [['相同'], [4, 1, 5, 6, 2]],
    #     [['未知'], [8, 1, 4, 7, 2]],
    #     [['不同'], [5, 5, 6, 1, 1]]
    # ]
    source_list = []
    source_one_hang_list = []   #source第一行数据
    source_one_hang_list.append(zhu_lie_title_name)
    for one in mubiao_list_all[0]:
        source_one_hang_list.append(one)

    print("source_one_hang_list:")
    print(source_one_hang_list)
    source_list.append(source_one_hang_list)

    #source第一行数据后几行数据
    source_houjihang_hang_shu = len(mubiao_list_all[0])
    print("source_houjihang_hang_shu:")
    print(source_houjihang_hang_shu)
    source_houjihang_yi_lie_shu = len(mubiao_list_all[1])
    print("source_houjihang_yi_lie_shu")
    print(source_houjihang_yi_lie_shu)  #后几行一列的数据


    for weidu_num in range(0,source_houjihang_yi_lie_shu):
        weidu_one_list = []
        weidu_one_name_list = []
        weidu_one_data_list = []

        weidu_one_name_list.append(mubiao_list_all[1][weidu_num])  #维度一条数据的第一个列表数据，记录名字
        #维度第二个列表的数据
        for hang_shu in range(0,source_houjihang_hang_shu):
            weidu_one_data_list.append(mubiao_list_all[hang_shu+2][weidu_num])  #维度一条数据的第二个列表数据，记录数据

        weidu_one_list.append(weidu_one_name_list)
        weidu_one_list.append(weidu_one_data_list)

        print("weidu_one_list:")
        print(weidu_one_list)
        source_list.append(weidu_one_list)

    print("source_list:")
    print(source_list)

    encode_value = source_one_hang_list[1]
    print("encode_value")
    print(encode_value)

    series_type_dict_list = []
    source_list_len = len(source_list)

    for i in range(1,source_list_len):
        series_type_dict_list.append(source_list[i])

    print('series_type_dict_list')
    print(series_type_dict_list)



    return render_template('mychar/staticbasethree.html',
                           titlename = zhu_lie_title_name,
                           pre_name_list = pre_name_list,
                           source_list = source_list,
                           item_name = zhu_lie_title_name,
                           encode_value = encode_value,
                           series_type_dict_list = series_type_dict_list,
                           hengzhou_name_list = hengzhou_name_list,
                           zongzhou_name_list = zongzhou_name_list

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

