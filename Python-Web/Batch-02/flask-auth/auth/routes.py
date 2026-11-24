from datetime import datetime, timezone

from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message

from db import db
from forms import RegisterForm
from models import User
from utils import generate_confirmation_token, send_mail, verify_confirmation_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    form = RegisterForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        new_user = User(email=email, first_name=first_name, last_name=last_name)
        new_user.set_password(plain_pwd=password)

        db.session.add(new_user)
        db.session.commit()

        token = generate_confirmation_token(new_user.email)
        mail_content = render_template(
            "emails/confirm.html", 
            name=new_user.first_name, 
            confirm_token=token
        )

        send_mail(
            subject="Verify your email",
            text_body="Confirm your email",
            html_body=mail_content,
            recipient=new_user.email
        )

        return "Registered. Please check your email inbox"
    return render_template("register.html", form=form)


@auth_bp.get('/confirm/<token>')
def confirm_email(token: str):
    email = verify_confirmation_token(token=token)

    if not email:
        return jsonify(
            {'error': "The confirmation link is invalid or expired"}
        ), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid token'}), 400
    elif user and user.is_verified:
        return jsonify({'message': "Account already confirmed"})

    user.is_verified = True
    user.verified_at = datetime.now(timezone.utc)
    login_user(user)

    db.session.commit()
    
    return redirect(url_for('auth.dashboard'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    
    if request.method == 'POST':
        form_data = request.form
        email = form_data.get('email')
        password = form_data.get('password')

        user: User = User.query.filter_by(email=email).first()
        if user is None:
            flash("Invalid credentials", category='red')
            return redirect(url_for('auth.login'))
        
        if user.check_password(plain_txt=password):
            login_user(user)
            flash("Login success", category='blue')
            return redirect('dashboard')
        
        flash("Invalid credentials", category='red')
        return redirect(url_for('auth.login'))


    return render_template('login.html')


@auth_bp.get('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@auth_bp.post('/logout')
@login_required
def logout():
    # if current_user.is_authenticated:
    logout_user()
    flash("Logout success")
    return redirect(url_for('auth.login'))
