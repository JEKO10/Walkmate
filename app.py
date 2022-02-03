from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisissecreykeywhichissecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    facebook = db.Column(db.String(50))
    location = db.Column(db.String(50))


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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data,
                        location=form.location.data, password=form.password.data, facebook=form.facebook.data)
        db.session.add(new_user)
        db.session.commit()

    return render_template("register.html", form=form)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if (__name__) == "__main__":
    app.run(debug=True)
