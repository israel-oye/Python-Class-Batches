from flask import current_app
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

CONFIRM_SALT = 'email-confirmation-salt'

def generate_confirmation_token(email: str):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=CONFIRM_SALT)


def verify_confirmation_token(token: str, max_age=1800):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = serializer.loads(token, salt=CONFIRM_SALT, max_age=max_age)
    except (SignatureExpired, BadSignature):
        return None
    return email


def send_mail(text_body, html_body, recipient, subject):
    from flask_mail import Message

    from app import mail

    mail_msg = Message(
        subject=subject,
        recipients=[recipient,],
        body=text_body,
        html=html_body
    )

    mail.send(mail_msg)
