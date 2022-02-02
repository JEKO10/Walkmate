from logging import PlaceHolder
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisissecreykeywhichissecret"
Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("remember")


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[InputRequired(), Email(
        message="Invalid email"), Length(max=50)])
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    facebook = StringField("facebook", validators=[
                           InputRequired(), Length(max=50)])
    location = StringField("location", validators=[
                           InputRequired(), Length(max=50)])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    form = LoginForm()

    return render_template("login.html", form=form)


@app.route("/register")
def register():
    form = RegisterForm()

    return render_template("register.html", form=form)


if (__name__) == "__main__":
    app.run(debug=True)
