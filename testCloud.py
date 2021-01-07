import jieba   #分词，把一个句子变成一个一个的词
from matplotlib import pyplot as plt   #绘图，数据可视化（点状图、柱形图、折线图等）
from wordcloud import WordCloud  #词云，用它来形成一个有遮罩效果的图形
from PIL import Image   #图片处理，验证码、图片后期处理等等
import numpy as np  #做矩阵运算用的，（中文显示，需要运算空间）
import sqlite3  #数据库


#准备词云所需的文字（词）
#查出词
# my_text = ''
# con = sqlite3.connect('movie.db')  #连接数据库
# cur = con.cursor()  #游标
# sql = 'select instroduction from movie250'  #数据库查询语句
# data = cur.execute(sql=sql)  #执行查询语句，得出查询后的结果
# for item in data:
#     my_text = my_text+item[0]   #如果不保存在本地变量中，查询出的数据会随着游标关闭和数据库连接关闭而消失，无法访问
# cur.close()  #关闭游标
# con.close()  #关闭数据库连接

#此处用字符串代替
my_text = "去年，山东省政协对省工商联提出的《关于促进支持民营经济发展政策落实的提案》、致公党山东省委会提出的《关于完善水利设施提升防涝抗旱能力的建议》、农工党山东省委会提出的《关于建立稳定脱贫长效机制的建议》3件重点提案进行了督办。不仅提案数量较上年进一步压缩，还都是集体提案，界别特色和党派优势进一步彰显"

#分词
my_text_cut = jieba.cut(my_text)  #使用cut函数自动分词
my_text_cut_string = ' '.join(my_text_cut)  #切好的词
print(my_text_cut)
print(my_text_cut_string)
print(len(my_text_cut_string))

#打开一张图，作为遮罩
my_img = Image.open(r'.\static\assets\img\girl.jpg')  #"./表示当前程序所在路径"  #打开遮罩图片
my_img_array = np.array(my_img)   #将图片转换为数组

#作词云
wc = WordCloud(
    background_color= 'white',  #输出图片的背景色
    mask=my_img_array,  #遮罩图片数组
    font_path='STCAIYUN.TTF', #字体文件名字  字体所在位置C:\Windows\Fonts
)

wc.generate_from_text(text=my_text_cut_string )  #从哪一个文本生成wc

#绘制图片
fig = plt.figure(1)  #1表示找第一个位置绘制出来
plt.imshow(wc)  #按照词云的规则来显示图片
plt.axis('off')  #是否显示坐标轴，off表示不显示

# plt.show()  #显示图片，显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'.\static\assets\img\girlwordgx.jpg',dpi=500)   #保存图片,dpi表示清晰度，默认为400，此处设置为500

