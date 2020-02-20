### log 2020.2.8 

**猛烈宇宙交響曲・第七楽章「無限の愛」**

这歌吉他真的有点吊，不对，是整体都很吊。之前看动画的时候只体会到了前半部分。

看.ass文件也知道，字体用了等距更纱黑体（Sarasa Gothic）。

歌词一开始基于网易云的版本，后面用uta-net的版本调整了一些写法（uta-net的歌词要获取到只要浏览器检查一下网页的元素就能获取到）

翻译基于网易云的版本，[叡山电车-改](https://cyl.moe/)，链接是翻译者的个人主页。

双语字幕真挺累的，这还是我在复制别人的工作的时候，一想到Ben Eater最近的视频20分钟还是很快的语速，这个时间要花的也太长了，感叹一句油管的自动字幕功能真好。

### log 2020.3

Ben Eater: What is a stack and how it works?

首先讲了利用subroutine能够减少重复的代码，但是由于利用到了跳转指令，所以程序执行会变慢，同时引入了子程序调用中需要用到的数据结构：栈。

### log 2020.2.11

- [x] obs timer: done 

- basic Django tutorial

**detailed tutorial setting**
- [x] pip setting(tsinghua)
- [x] install system-wide uWSGI and Django
- [x] install nginx and start service

Tips:
1. Django中Project和App的关系：包含关系
2. essential location: /etc/nginx/nginx.conf & uwsgi_params
3. 排错日志：/var/log/nginx/error.log access.log
4. TCP port: 自定义的conf监听8000端口，转给django 8001；同时需要修改default（默认监听80端口，返回Nginx欢迎界面），也转给django 8001端口
5. Unix sockets instead of ports: default和site.conf都要改，配合ini使用uwsgi
6. 部署线上时最大的区别在于权限（注意看日志），664不够，要666
7. supervisor也是sudo安装即可。配置文件写好初始化一下，就能start了。

```
# for task 1
Start-Process -NoNewWindow python .\timer.py
# for task 2
# system-wide installation: 
sudo pip3 install django & uwsgi
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# the web client <-> uWSGI <-> Django
uwsgi --http :8000 --module mysite.wsgi

# the web client <-> the web server
sudo /etc/init.d/nginx start    # start nginx
```