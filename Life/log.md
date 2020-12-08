# Logs

## log 2020.2.8 

**猛烈宇宙交響曲・第七楽章「無限の愛」**

这歌吉他真的有点吊，不对，是整体都很吊。之前看动画的时候只体会到了前半部分。

看.ass文件也知道，字体用了等距更纱黑体（Sarasa Gothic）。

歌词一开始基于网易云的版本，后面用uta-net的版本调整了一些写法（uta-net的歌词要获取到只要浏览器检查一下网页的元素就能获取到）

翻译基于网易云的版本，[叡山电车-改](https://cyl.moe/)，链接是翻译者的个人主页。

双语字幕真挺累的，这还是我在复制别人的工作的时候，一想到Ben Eater最近的视频20分钟还是很快的语速，这个时间要花的也太长了，感叹一句油管的自动字幕功能真好。

## log 2020.3

Ben Eater: What is a stack and how it works?

首先讲了利用subroutine能够减少重复的代码，但是由于利用到了跳转指令，所以程序执行会变慢，同时引入了子程序调用中需要用到的数据结构：栈。

## log 2020.2.11

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

```bash
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

## 2020.2.21

思路：crontab 配合Nginx日志

[cron](https://linux.vbird.org/linux_basic/centos7/0430cron.php)
[Java思路](http://huyan.couplecoders.tech/java/redis/nginx/2019/05/10/监听nginx日志实现博客访问计数/)
[面试题](https://blog.csdn.net/u010590166/article/details/17242181)
[log-parsing](https://easyengine.io/tutorials/nginx/log-parsing/)
[nginx official](https://www.nginx.com/blog/sampling-requests-with-nginx-conditional-logging/)
“侦测主机流量的咨询”：

- 流量
- 线上人数侦测

## 3.18 

### HTTPS

- 申请证书和审核（阿里云），以及下载，通过RCP转递文件
- 首先在nginx.conf配置证书和key
- (1) https.conf 监听443端口，80端口添加rewrite (2) 改进了一下，将mysite监听的从8000转为443
- Django 添加SSL相关选项
- ALLOWED_HOST 添加一个不用www的地址。
- 最先的排错从400 Bad Request 开始

[nginx-https-best](https://www.cnblogs.com/kevingrace/p/6187072.html)
[nginx-https-aliyun](https://help.aliyun.com/document_detail/98728.html?spm=5176.2020520163.cas.21.701fcDjvcDjvfG)
[rcp](https://help.aliyun.com/document_detail/51935.html?spm=5176.10695662.1996646101.searchclickresult.26c45522vRQVhI)

```
# On Ubuntu WSL:
sudo service cron start
```

## 4.7
Node.js Introduction

ECMAScript: ECMAScript 和 JavaScript 的关系是，前者是后者的规格，后者是前者的一种实现

**REPL**: Read Eval Print Loop

## 5.9

Ctrl + F5, 强制刷新，默认清除了缓存

设计思路：

- games.html 纯HTML+CSS+JS
- produce.html 加入VUE要素的设计
- monitor VUE和Django结合
- blog VUE和Django结合

## 6.23

Online Judge：

- 从数据库获取获取题目描述、输入测试、输出结果(Database Problems)
- 用户通过浏览器输入，产生POST请求传输数据，形成代码文件，（安全检查），执行捕获输出和错误信息
- 反馈信息回传，提交记录写入数据库(Database Submission)

admin.css缺失跟nginx配置有关，原来应该通过static_root解决，不再需要App内Static

## 2020.7.2

- 采用Git来维护Django的App，同时再次修改了一波Static路径来保证能同步。

### 去除双系统

[方法5](https://blog.csdn.net/qq_15192373/article/details/81536602)

```bash
> diskpart
> list disk-------------------------列出系统中拥有的磁盘
> select disk 0--------------------选择EFI引导分区所在的磁盘，请根据实际情况选择
> list partition--------------------列出所选磁盘拥有的分区
> select partition 1---------------选择EFI引导分区，类型为系统的分区，就是EFI引导分区
> assign letter=p-----------------为所选分区分配盘符，请分配空闲盘符
```

> 根据实际情况选到EFI的分区。显示出分区后，通过带管理员权限的Powershell来进入P盘

```bash
cd P:/[EFI]
rm -r [ubuntu]
```

## 2020.09


## 2020.11

- Django 结合Redis，配合RestFramework，做了个大概。在api APP中

- 下一步是整体上docker [django-on-docker](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

- 
