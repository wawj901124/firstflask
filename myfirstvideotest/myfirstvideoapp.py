from flask import Flask   #导入FLask类
from flask import render_template   #导入render_template，叫渲染模板，帮助把想要的渲染文件给展示出来
from flask import Response   #导入Response
from flask_bootstrap import Bootstrap  #导入Bootstrap
from testbootstrap.myform import NameForm
import os

from importlib import import_module

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from myfirstvideotest.camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera


#Flask类接收一个参数__name__
app = Flask(__name__)   #初始化了一个对象，叫app
app.config['SECRET_KEY'] = 'hard to guess string'    #设置scrftoken
bootstrap = Bootstrap(app)   #初始化flask_bootstrap





#首页
@app.route('/',methods=['GET','POST'])      #设置路径访问为get和post,不设置默认为get
def index():  #函数的名字可以随便起，只要符合python函数的命名规则就行
    name = None
    form = NameForm()
    if form.validate_on_submit():  #表单提交有效
        name = form.name.data   #将表单内容复制给变量name
        form.name.data = ''  #置空表单内容
    return render_template('index.html',
                           name=name,
                           form = form
                           )

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    bootstrap.run()   #调用run方法，启动服务器
                #服务器默认没有开启debug模式,即做了修改之后，不会实时更新，需要关闭服务器重启才能生效
    # app.run(debug=True)    #开启调试模式，但是不一定有效，因为在不同的开发环境中，有的有效，有的没有效
    #flask默认开启的网站是本地的：127.0.0.1:5000
    #现在把已经有的本机访问改成局域网
    #host='0.0.0.0'，配置host为0.0.0.0
    #port = 8080,配置端口
    #访问服务器的ip地址即可
    # app.run(host='0.0.0.0',port = 8080)

