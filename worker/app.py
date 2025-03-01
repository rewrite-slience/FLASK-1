from flask import Flask,session,g
import config
from external import db,mail
from blueprint.qa import bq as qa_bp
from blueprint.auth import bp as auth_bp
from flask_migrate import Migrate
from model import Usermodel



app = Flask(__name__)
app.config.from_object(config)  # 从类加载配置
db.init_app(app)
mail.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

migrate = Migrate(app, db)

@app.before_request
def before_request():
    user_id=session.get("user_id")
    if user_id:
        user=Usermodel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)
    
@app.context_processor
def context_processor():
    return {"user":g.user} 




@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)