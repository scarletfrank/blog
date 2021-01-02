# ldap记

> Metabase开源版中的LDAP验证究竟是什么

## LDAP

*Lightweight Directory Access Protocol* 缩写为LDAP：它是一种查询或者修改 X.500标准下的目录服务的协议。

## 关键

在进入具体操作前，先记住：

本质是LDAP服务器端，搭起一个带有特定监听的服务器（IP及389端口），客户端需要配置服务器地址后，用一定的LDAP已有Admin用户登录，结合一定的查询条件（例如某机构下），得到对应的用户结果（用户名及密码），验证通过就放行，进入Metabase系统

## 



## 参考资料

[core-service](https://ubuntu.com/server/docs/service-ldap)