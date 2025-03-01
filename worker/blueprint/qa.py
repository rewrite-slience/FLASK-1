from flask import Blueprint,render_template,request,session,g,redirect,url_for
from .forms import Public_question,AnswerForm
from model import QuestionModel,AnswerModel
from external import db
from decorators import  login_required


bq=Blueprint("qa",__name__,url_prefix="/")
@bq.route("/")
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html",questions = questions)
@bq.route("/qa/public",methods=['GET','POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form =Public_question(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # TODO:跳转到这篇回答的问答
            return redirect("/")
        else:
            print(form.errors)
            return  redirect("/qa/public")
@bq.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)
@bq.post("/answer/public")#新的写法
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content,question_id=question_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail",qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail",qa_id=request.form.get("question_id")))
@bq.route("/search")
def QaSearch():
    q=request.args.get("q")
    question= QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html", questions=question)


     
    












