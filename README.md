# IBM website

临时体验网址：

http://119.23.73.156:8001/mysite/application/

## 文件结构

forum #虚拟环境

forum_logs #开发日志

IBMsite #项目源码

requirements.txt #项目依赖

## 环境依赖：

  * git(可选)
  * python2.7 or 3.5，推荐2.7
  * pip
  * virtualenv
  * mysql

## 安装：

### 从github上下载源码

    git clone https://github.com/USER0308/IBMclubBBS

或打开网址下载zip解压

### 进入 IBMclubBBS 文件夹

    cd IBMclubBBS

### 创建虚拟环境

    virtualenv env

### 激活虚拟环境

    source env/bin/activate

### 安装依赖模块

    pip install -r requirements.txt

### 修改 IBMsite/IBMsite/settings.py 中数据库帐号密码

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'forumdb',
    		'USER': 'root',
    		'PASSWORD': 'root',
    		'HOST': '127.0.0.1',
        }
    }

把数据库帐号密码改为本机数据库帐号密码

### 创建数据库

    create database forumdb default charset utf8 collate utf8_general_ci

### 同步数据库

    python ./manage.py migrate

    python ./manage.py makemigrations

### 创建后台管理员

    python ./manage.py createsuperuser

### 启动服务

    python ./manage.py runserver

### 访问网站

http://127.0.0.1:8000/mysite/application

### 创建系统管理员，负责发送邀请码

http://127.0.0.1:8000/admin

先在member_models中创建一个member对象，然后在manager_models中将manager对象指向该member，position 填 admin

### 正常使用

申请 http://127.0.0.1:8000/mysite/application

注册 http://127.0.0.1:8000/mysite/sign_up

登录 http://127.0.0.1:8000/mysite/login
