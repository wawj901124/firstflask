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

#主流程
def main():
    create_db(dbpath) #初始化数据库
    jobURLs = getURLs(pagenum)
    for url in jobURLs:
        getData(url)

    #将爬取到的数据保存到数据库
    print(datalist)
    saveData()



if __name__ ="__main__":
    main()