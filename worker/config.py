## MySQL所在的主机名
HOSTNAME = "127.0.0.1" # MySQL服务器的IP地址或主机名，默认为3306
## 连接MySQL的端口号
PORT = 3306
## 连接MySQL的用户名
USERNAME = "root"
## 连接MySQL的密码
PASSWORD = "123456"
## MySQL上的远程数据库名称
DATABASE = "page"

DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI
SECRET_KEY="123432asa"


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3221951064@qq.com"
MAIL_PASSWORD = "siiqpxrdxbdqchfj"
MAIL_DEFAULT_SENDER = "3221951064@qq.com"
# usouxpqyglcgb`