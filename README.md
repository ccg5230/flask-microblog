flask框架简单web项目，简要说明如下：
=========================

项目使用包清单见：requirements.txt<br>

大版本：python3.7 cenos7（vm虚拟机） flask1.0.2 <br>
使用virtualenv + uwsgi 运行<br>

主要功能块：
------------
Flask<br>
SQLAlchemy <br>
sqlite3：cenos7自带，你也可以替换config.py配置<br>
Flask-Migrate:SQLAlchemy的一个数据库迁移框架<br>
Elasticsearch6.6.2全文搜索<br>
Python任务队列是Redis Queue：我使用的是windows版本Redis，未启动哨兵模式，当然linux安装更方便<br>
Flask-Bootstrap：插件，便于模板开发<br>
Restful APi + Token:app/api包下，当然你也可以使用Restless插件<br>

环境变量配置如下
--------------
vim /etc/profile (windows需要设置系统环境变量)<br>
export JAVA_HOME=/usr/local/java/jdk1.8.0_191/<br>
export CLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar<br>
export PATH=$PATH:${JAVA_HOME}/bin<br>
export ELSEARCH_HOME=/usr/local/elasticsearch-6.6.2<br>
export PATH=$PATH:${ELSEARCH_HOME}/bin<br><br>
export REDIS_URL=redis://192.168.16.57:6379<br>

错误邮件邮箱配置
----------------
export MAIL_SERVER=smtp.sina.com #查看你的邮箱服务器配置<br>
export MAIL_PORT=587<br>
export MAIL_USE_TLS=1<br>
export MAIL_USERNAME=mailname #需要替换<br>
export MAIL_PASSWORD=mailpassword #需要替换<br>
export ADMINS=xxx@sina.com #需要替换<br>
export MS_TRANSLATOR_KEY=is_not_have<br><br>
export ELASTICSEARCH_URL=http://localhost:9200<br>
