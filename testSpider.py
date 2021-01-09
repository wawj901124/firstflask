import sqlite3

dbpath = './job.db'

def create_db(dbpath):
    sql = """
            create table job
            (
             id integer primary key autoincrement,
             job_link text,
             jname varchar ,
             cname varchar,
             area varchar ,
             salary text,
             educate text,
             info text
            )
    """ #创建数据表
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def saveData(datalist,dbpath):
    create_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur= conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index ==4 or index ==5:
                continue
            data[index] = '"'+data[index]+'"'
            sql = """
                    insert into job(
                    job_link,
                    jname  ,
                    cname ,
                    area  ,
                    salary ,
                    educate ,
                    info
                    ) values (%s)
            """%",".join(data)    #插入内容
            print(sql)
            cur.execute(sql)
            conn.commit()  #保存数据到数据库，必须要用commit函数提交
        cur.close()  #关闭游标
        conn.close() #关闭数据库连接


from bs4 import BeautifulSoup  #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib,request,urllib.error  #制定url,获取网页数据
import xlwt  #进行excel操作
from urllib import parse  #parse,解析


KW = input("请输入您要搜索的岗位关键字：")
keyword = parse.quote(parse.quote(KW) ) #将汉字解析为url中的内容


#主流程
def main():
    url = "https://search.51job.com/list/090200,000000,0000,00,9,99,"+keyword+",2,1.html"
    print(url)
    # #1.爬取网页
    # datalist = getData(baseurl)
    # # create_db(dbpath) #初始化数据库
    # dbpath = "movie.db"
    # #3.保存数据
    # #saveData(datalist,dbpath)
    # saveData2DB(datalist,dbpath)
    # jobURLs = getURLs(pagenum)
    # for url in jobURLs:
    #     getData(url)
    #
    # #将爬取到的数据保存到数据库
    # print(datalist)
    # saveData()


#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,1):  #调用获取页面信息的函数，10次
        url = baseurl+str(i*25)
        html = askURL(url)  #保存获取到的网页源码

        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            pass

    return  datalist

#得到指定一个url的网页内容
def askURL(url):
    pass



if __name__ =="__main__":
    main()