from external import db 
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from  datetime import datetime

class Usermodel(db.Model):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True, autoincrement=True)
    username=Column(String(100),nullable=False)
    password=Column(String(100),nullable=False)
    eamil=Column(String(100),nullable=False,unique=True)
    join_time=Column(DateTime,default=datetime.now)
class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    email = db.Column(db.String(100),nullable = False)
    captcha = db.Column(db.String(100),nullable = False)
class QuestionModel(db.Model):
    __tablename__ ="question"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    #外键
    author_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    author = db.relationship( Usermodel,backref="questions")
class AnswerModel(db.Model):
    __tablename__="answer"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    #外键
    question_id = db.Column(db.Integer,db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    #关系
    question = db.relationship(QuestionModel,backref=db.backref("answers",order_by=create_time.desc()))
    author = db.relationship(Usermodel, backref="answers")
    