from flask_wtf import FlaskForm   #导入 FlaskForm 表单
from wtforms import StringField,SubmitField  #导入表单字段类型
from wtforms.validators import DataRequired  #导入验证函数DataRequired（），验证内容不为空

class NameForm(FlaskForm):
    name = StringField('what is you name',validators=[DataRequired()])  #DataRequired()验证数据有效性，确保内容不为空
    submit = SubmitField('submit')  #提交按钮，名字为submit


# #WTForms支持的HTML标准字段：
# 字段类型                               说明
# BooleanField                        复选框，值为True和False
# DateField                           文本字段，值为datetime.date格式
# DateTimeField                       文本字段，值为datetime.datetime格式
# DecimalField                        文本字段，值为decimal.Decimal
# FileField                           文件上传字段
# HiddenField                         隐藏的文本字段
# MultipleFileField                   多文件上传字段
# FieldList                           一组指定类型的字段
# FloatField                          文本字段，值为浮点数
# FormField                           把一个表单作为字段嵌入另一个表单
# IntegerField                        文本字段，值为整数
# PasswordField                       密码文本字段
# RadioField                          一组单选按钮
# SelectField                         下拉列表
# SelectMultipleField                 下拉列表，可选择多个值
# SubmitField                         表单提交按钮
# StringField                         文本字段
# TextAreaField                       多行文本字段

# #WTForms内建的验证函数：
# 验证函数                                    说明
# DataRequired                              确保转换类型后字段中有数据
# Email                                     验证电子邮件地址
# EqualTo                                   比较两个字段的值，常用于要求输入两次密码进行确认的情况
# InputRequired                             确保转换类型前字段中有数据
# IpAddress                                 验证IPv4网络地址
# Length                                    验证输入字符串的长度
# MacAddress                                验证MAC地址
# NumberRange                               验证输入的值在数字范围之内
# Optional                                  允许字段中没有输入，将跳过其他验证函数
# Regexp                                    使用正则表达式验证输入值
# URL                                       验证URL
# UUID                                      验证UUID
# AnyOf                                     确保输入值在一组可能的值中
# NoneOf                                    确保输入值不在一组可能的值中

