## 项目概述

### 1.介绍

- 此项目名为网上购书商务系统，用来模拟实际生活中的图书网购场景，使用者分为商家和顾客两个群体

- 项目整体是基于 `Python+Django` 的`Web`框架，后端存储数据库使用的是`MySQL`，前端网页设计使用的是 `Bootstrap` 框架（借鉴的是网上的模板），数据库可视化工具可以使用`Navicat`   

  <br>
  
  


### 2.功能划分

**商家层面：**

- 商家可以在网页进行注册和登录； 
- 商家可以查询、修改和增删书籍出版社信息，包括书籍出版社名称和书 籍出版社地址； 
- 商家可以查询、修改和增删书籍作者信息，包括作者姓名、性别、年龄 和联系方式； 
- 商家可以查询、修改和增删每一本书籍的具体信息，包括书名、书籍的 ISBN、出版社、作者、出版日期和库存量； 
- 商家可以实时查看顾客的订单信息，但没有权限修改； 
- 商家页面内提供检索功能，商家输入关键字可迅速检索带有该关键字的 记录。

**顾客层面：**

- 顾客可以在网页进行注册和登录； 
- 顾客可以在查询每一本书籍的具体信息，但没有权限修改； 
- 顾客可以选中某一本书籍后可以创建订单，填写书名、顾客姓名、购买 数量、联系方式和地址； 
- 顾客可以修改已创建订单的信息； 
- 顾客页面内提供检索功能，顾客输入关键字可迅速检索带有该关键字的记录。  

  <br>

  

### 3.概念结构

- **作者实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/16.png" alt="img" style="zoom:50%;" />

- **书籍实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/17.png" alt="img" style="zoom:50%;" />

- **出版社实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/18.png" alt="img" style="zoom:50%;" />

- **订单实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/19.png" alt="img" style="zoom:50%;" />

- **商家实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/20.png" alt="img" style="zoom:50%;" />



- **顾客实体型结构**

<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/21.png" alt="img" style="zoom:50%;" />

- **整体E-R图**



<img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/22.png" alt="img" style="zoom: 80%;" />

  <br>

  

## 系统实现

### 1.实现流程

- 先确保已经启动MySQL服务和创建数据库`bms`，并进入`Web_bookshop_system/library_bms/bms/setting.py`中，将PASSWORD修改为你的MySQL登陆密码![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/11.png)

- 在命令行中输入代码创建Django内置表结构：`python manage.py migrate` 

- 接着在命令行中输入命令让 Django知道我们自定义模型有一些变更,并根据我们自定义app的模型生成创建数据表的脚本：`python manage.py makemigrations app01`

- 然后通过命令创建app01模型对应的数据库表：`python manage.py migrate app01`，得到如下表结构

  <img src="https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/12.png" alt="img" style="zoom:67%;" />

- 最后在终端进入路径`Web_bookshop_system/library_bms`，运行`python manage.py runserver 127.0.0.1:8000`，接着任意选择一个浏览器并输入`127.0.0.1:8000`就可以进入登录界面

  <br>

  

### 2.数据表

数据表存储的内容要与`商家界面`和`顾客界面`所显示的保持一致，例如

- **书籍信息**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/13.png)

  

- **订单信息**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/14.png)

  

- **出版社信息**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/15.png)

  <br>





  

## 演示效果

### 1.商家视角

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

​    <br>

### 2.顾客视角

- **顾客登录**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/6.png)

  

- **顾客选购图书创建订单**

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/7.png)

  

- **顾客查看订单**（进行修改或退订）

![img](https://raw.githubusercontent.com/ChongbinZhao/Web_bookshop_system/master/src/8.png)

  <br>