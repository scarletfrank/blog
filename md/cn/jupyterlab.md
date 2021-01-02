# Jupyter Lab

> 如题。群里闲聊安利WSL成功，顺便聊起`jupyterlab`的配置，就有了下面的实践

## 分析

`JupyterLab`是这个项目下一代的网页端界面。也就是说服务器上有一个server进程，接受浏览器发出的请求做出响应。

### 安装

这个不多说。`python3 -m pip install jupyterlab` 

### 简易管理

`lab`文档里虽然没写，但`notebook`里有写如何做一个服务器。通过

```shell
jupyter lab --generate-config
# 进入 ~/.jupyter/jupyter_notebook_config.py
# 其实这个文件里对各项参数解释的很清楚，包括如何生成密码
# 简易管理这里改的多一点，主要是
# 1. 允许远程访问及所有IP访问（开放端口）
# 2. 设置对外监听端口及密码
# 3. 不开启浏览器
jupyter lab # 启动程序
```

### 复杂管理

上面的命令自己面前的机器用一下还行，但如果要保存日志及长期运行，就不太行了。网上还有一种方法是用`nohup jupyter lab &`的方式，长期运行并保留输出日志，但关闭就需要先查看进程手动关闭，重启不是特别的方便，以及如果是想和现有的`Nginx`合并，就需要换个思路

所以 => **Nginx + Supervisor**

1. Nginx中加一个新配置，将外部请求通过`proxy_pass`转至本地（不通过Jupyter监听全局）

2. Supervisor配一个`[program: lab]`，可以轻松restart。