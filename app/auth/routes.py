from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
from . import auth_bp
from .forms import SignupForm, LoginForm
from .models import User


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))
    form = SignupForm()
    error = None
    context = {
        'form': form,
        'title': 'Sign-up Example - Semantic',
        'error': error
    }
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            error = (
                f"El email {email} ya está siendo utilizado por otro usuario"
            )
        else:
            # Creamos el usuario y lo guardamos
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get("next", None)
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("public.index")
            return redirect(next_page)
    return render_template("auth/signup_form.html", **context)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))
    form = LoginForm()
    error= None
    context = {
        'form': form,
        'title': 'Login Example - Semantic',
        'error': error
    }
    if form.validate_on_submit():
        email = form.email.data
        user = User.get_by_email(email=email)
        if user is None:
            context['error'] = f"El email {email} no se enuentra registrado."
            print(context)
            return render_template("auth/login_form.html", **context)
        
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("public.index")
            return redirect(next_page)

        if user is not None and not user.check_password(form.password.data):
            context['error'] = f"El email {email} no se enuentra registrado."
            return render_template("auth/login_form.html", **context)
        

    return render_template("auth/login_form.html", **context)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("public.index"))


@login_manager.user_loader
def load_user(user):
    return User.query.get(int(user))
