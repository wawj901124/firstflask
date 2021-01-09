from bs4 import BeautifulSoup

html = open("jobList.html","r")  #以只读的方式读取jobList.html文件

bs =BeautifulSoup(html,"html.parser")  #解析成html,解析的方式就是html.parser
                                       #实例化一个bs对象

# resultList = bs.select("#resultList")  #同过select函数定位到id=resultList的内容
resultList = bs.select(".j_result")  #同过select函数定位到classname=resultList的内容

print(resultList)
