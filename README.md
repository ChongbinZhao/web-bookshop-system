#### 演示效果

##### 1.商家界面

- **商家登陆界面**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/1.png)



- **商家编辑出版社信息**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/2.png)



- **商家编辑书籍作者信息**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/3.png)



- **商家编辑书籍信息** 

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/4.png)



- **商家查看用户订单**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/5.png)



##### 2.顾客界面 

- **顾客登录**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/6.png)



- **顾客选购图书创建订单**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/7.png)



- **顾客查看订单**（进行修改或退订）

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/8.png)





#### 系统实现

##### 1.技术栈  

编程语言：Python

Web框架：Django

前端实现：HTML+CSS+js（借鉴的是网上的模板）

数据库：MySQL

数据库可视化工具：Navicat



##### 2.复现流程

- 先确保已经启动MySQL服务，并进入`Web_bookshop_system/library_bms/bms/setting.py`中，将PASSWORD修改为你的MySQL登陆密码![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/11.png)

- 在命令行中输入代码创建Django内置表结构：`python manage.py migrate` 

- 接着在命令行中输入命令让 Django知道我们自定义模型有一些变更,并根据我们自定义app的模型生成创建数据表的脚本：`python manage.py makemigrations app01`

- 然后通过命令创建app01模型对应的数据库表：`python manage.py migrate app01`，得到如下表结构

  <img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/12.png" alt="img" style="zoom:67%;" />

- 最后在终端进入路径`Web_bookshop_system/library_bms`，运行`python manage.py runserver 127.0.0.1:8000`，接着就可以登录网上购书商务系统进行一系列操作了