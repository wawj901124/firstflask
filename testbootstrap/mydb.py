from flask_sqlalchemy import SQLAlchemy  #导入SQLAlchemy
from app import app #导入app
import os

basedir = os.path.abspath(os.path.dirname(__file__))   #当前文件的路径

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')+'/test.db'    #配置数据库路径

# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db =SQLAlchemy(app)   #实例化数据库实例

#建表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# #db配置与说明
# 名字	                                        备注
# SQLALCHEMY_DATABASE_URI	                    用于连接的数据库 URI 。例如:sqlite:////tmp/test.dbmysql://username:password@server/db
# SQLALCHEMY_BINDS	                        一个映射 binds 到连接 URI 的字典。更多 binds 的信息见用 Binds 操作多个数据库。
# SQLALCHEMY_ECHO	                            如果设置为Ture， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。(打印sql语句)
# SQLALCHEMY_RECORD_QUERIES	                可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见get_debug_queries()。
# SQLALCHEMY_NATIVE_UNICODE	                可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于 一些数据库适配器是必须的（比如 Ubuntu 上 某些版本的 PostgreSQL ）。
# SQLALCHEMY_POOL_SIZE	                    数据库连接池的大小。默认是引擎默认值（通常 是 5 ）
# SQLALCHEMY_POOL_TIMEOUT	                    设定连接池的连接超时时间。默认是 10 。
# SQLALCHEMY_POOL_RECYCLE	                    多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定 这个值为 2 小时

# #常用的SQLAlchemy字段类型
# 类型名	           python中类型	            说明
# Integer	           int	                    普通整数，一般是32位
# SmallInteger	   int	                    取值范围小的整数，一般是16位
# BigInteger	       int或long	            不限制精度的整数
# Float	           float	                浮点数
# Numeric	           decimal.Decimal	        普通整数，一般是32位
# String	           str	                    变长字符串
# Text	           str	                    变长字符串，对较长或不限长度的字符串做了优化
# Unicode	           unicode	                变长Unicode字符串
# UnicodeText	       unicode	                变长Unicode字符串，对较长或不限长度的字符串做了优化
# Boolean	           bool	                    布尔值
# Date	           datetime.date	        时间
# Time	           datetime.datetime	    日期和时间
# LargeBinary	       str	                    二进制文件


# #常用的SQLAlchemy列选项
# 选项名	                              说明
# primary_key	                          如果为True，代表表的主键
# unique	                              如果为True，代表这列不允许出现重复的值
# index	                              如果为True，为这列创建索引，提高查询效率
# nullable	                          如果为True，允许有空值，如果为False，不允许有空值
# default	                              为这列定义默认值

# #常用的SQLAlchemy关系选项
# 选项名	                           说明
# backref	                           在关系的另一模型中添加反向引用
# primary join	                   明确指定两个模型之间使用的联结条件
# uselist	                           如果为False，不使用列表，而使用标量值
# order_by	                       指定关系中记录的排序方式
# secondary	                       指定多对多关系中关系表的名字
# secondary join	                   在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件