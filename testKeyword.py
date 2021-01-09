from urllib import parse  #parse,解析

keyword = parse.quote("大数据")  #将汉字解析为url中的内容
newKW = parse.quote(keyword)  #再转义一次,可以将第一次的转义的百分号转为百分之25

threeKw = parse.quote(newKW)

print(keyword)
print(newKW)
print(threeKw)