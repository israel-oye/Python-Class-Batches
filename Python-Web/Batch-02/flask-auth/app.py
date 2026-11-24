from flask import Flask, render_template
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect

import config
from auth.routes import auth_bp
from db import db, migrate
from models import User
from pages.routes import page_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.MAIL_FROM
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_DEBUG'] = False
app.config["MAIL_DEFAULT_SENDER"] = config.MAIL_FROM

db.init_app(app)
migrate.init_app(app)
login_manager = LoginManager(app)
csrf_protect = CSRFProtect(app)
mail = Mail(app)

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'red'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(page_bp, url_prefix='/home')

# with app.app_context():
#     db.create_all()

@login_manager.user_loader
def load_user(uuid):
    return User.query.get(uuid)

@app.route('/send-mail')
def send_mail():
    html_body = render_template('emails/welcome.html', user='Lagbaja')

    msg = Message(
        subject="Test Mail",
        recipients=["walon59287@bcough.com"],
        body=f"Hello world. Testing email sending",
        html=html_body,
        sender=config.MAIL_FROM,
    )
    # try:
    mail.send(msg)
    return "Sent email"

if __name__ == '__main__':
    app.run(debug=True)
