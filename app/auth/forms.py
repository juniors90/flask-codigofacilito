"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/01/2019

"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField("Name", render_kw={"placeholder": "Name"}, validators=[DataRequired(), Length(max=64)])
    password = PasswordField("Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    email = StringField("E-mail address", render_kw={"placeholder": "E-mail address"}, validators=[DataRequired(), Email()])
    submit = SubmitField("Registrar")


class LoginForm(FlaskForm):
    email = StringField("E-mail address", render_kw={"placeholder": "E-mail address"}, validators=[DataRequired()])
    password = PasswordField("Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Login")
