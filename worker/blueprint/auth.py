from flask import Blueprint ,render_template,jsonify,redirect,url_for,session
from flask_mail import Message
from external import mail,db
from flask import request
import string
import random
from model import EmailCaptchaModel,Usermodel
from .forms import RegisterForm,LoginForm
bp=Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template("login.html")
    else:
         form=LoginForm(request.form)
         if form.validate():
            email=form.email.data
            password=form.password.data
            user = Usermodel.query.filter_by( eamil=email).first()
            if not user:
                print("邮箱不存在")
                return redirect(url_for("auth.login"))
            if  password==user.password:
                session["user_id"]=user.id
                return redirect("/")
            else:
                print("密码错误")
                return redirect(url_for("auth.login"))
    return redirect(url_for("auth.login"))

@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method =='GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # #表单验证:flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = Usermodel( eamil=email,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/mail/test")
def Mailtest():
    message=Message(subject="邮箱测试",recipients=["3221951064@qq.com"],body="test")
    mail.send(message)
    return "发送成功"
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")

    # 4/6: 随机数组、宁母、数组和字母的组合
    source = string.digits*4
    captcha = random.sample(source,4)
    # print(captcha)
    captcha="".join(captcha)
    message = Message(subject="知了传课验证码", recipients=[email], body=f"您的验证码是{captcha}")
    mail.send(message)
    # memcached/redis
    # 用数据库表的方式存储
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    return jsonify({"code": 200,"message":"","data": None})
@bp.route("/logout")
def logout():
    session.clear()
    #清除session信息
    return redirect("/")


