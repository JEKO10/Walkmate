from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisissecreykeywhichissecret"


class LoginForm(FlaskForm):
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("remember")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    form = LoginForm()

    return render_template("login.html", form=form)


if (__name__) == "__main__":
    app.run(debug=True)
