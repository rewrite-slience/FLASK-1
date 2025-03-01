import wtforms
import wtforms.form
from wtforms.validators import Email,Length,EqualTo,InputRequired
from model import Usermodel,EmailCaptchaModel
from external import  db
class RegisterForm(wtforms.Form):  
    email = wtforms.StringField("email",validators=[Email(message="邮箱格式错误!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="两次输入密码不一致")])
    def validate_eamil(self, field):
        email=self.email.data
        user=Usermodel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="邮箱已经被注册")
    def vaidate_captcha(self,field):
        captemcha=field.data
        email=self.email.data
        captermodel=EmailCaptchaModel.query.filter_by(email=email,captemcha=captemcha).first()
        if  not captermodel:
              raise wtforms.ValidationError(message="注册玛错误")
        else:
            db.session.delete(captermodel)
            db.session.commit()
class LoginForm(wtforms.Form):
     email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
     password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误!")])
class Public_question(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3,max=100,message="标题格式错误!")])
    content = wtforms.StringField(validators=[Length(min=3,message="内容格式错误!")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3,message="内容格式错误!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id!")])



        

