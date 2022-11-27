"""import os"""
import os
import flask
from dotenv import load_dotenv, find_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for, request, flash
import requests
from flask_login import (
    login_user,
    login_required,
    UserMixin,
    LoginManager,
    logout_user,
    current_user,
)

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

app.secret_key = "groupproject"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """load user"""
    return Persons.query.get(int(user_id))


class Persons(UserMixin, db.Model):
    """create table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100))

with app.app_context():
    db.create_all()


@app.route("/")
def signup_page():
    "define signup page"
    return flask.render_template("signup.html")


@app.route("/signup", methods=["GET", "POST"])
def handle_signup():
    """handle signup page"""
    user_name = request.form.get("Username")
    password = request.form.get("Password")

    
    user = Persons.query.filter_by(username=user_name).first()

    if user_name  == "":
        flash("Invalid Response. Please enter all fields to signup")
        return redirect(url_for("signup_page"))

    if password == "":
        flash("Invalid Response. Please enter all fields to signup")
        return redirect(url_for("signup_page"))



    if user:
        flash("Username exists. Please enter different user or click login")
        return redirect(url_for("signup_page"))

    
    newUser = Persons(username=user_name, password = generate_password_hash(password, method='sha256'))
    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for("login_page"))


@app.route("/news")
@login_required
def top_ten_news():
    """define news function"""
    nyt_search_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    response = requests.get(
        nyt_search_url,
        params={
            "api-key": os.getenv("NYT_ARTICLE_SEARCH_API_KEY"),
        },
        timeout=10,
    )

    json_data = response.json()
    article_objects = json_data["response"]["docs"]

    recent_ten_news = article_objects
    user = current_user.username
    return flask.render_template(
        "news.html", recent_ten_news=recent_ten_news, user=user
    )


@app.route("/top selling books")
@login_required
def top_selling_books():
    """define current best selling books"""
    nyt_best_selling_book_url = (
        "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"
    )

    response = requests.get(
        nyt_best_selling_book_url,
        params={
            "api-key": os.getenv("NYT_ARTICLE_SEARCH_API_KEY"),
        },
        timeout=10,
    )

    json_data = response.json()
    books_objects = json_data["results"]["books"]
    user = current_user.username
    return flask.render_template("books.html", books_objects=books_objects, user=user)


@app.route("/login")
def login_page():
    """login page"""
    return flask.render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def handle_login():
    """handle login form"""
    user_name = request.form.get("Username")
    passcode = request.form.get("Password")


    checkuser = Persons.query.filter_by(username=user_name).first()

    if user_name  == "":
        flash("Invalid Response. Please enter all fields to login")
        return redirect(url_for("login_page"))

    if passcode == "":
        flash("Invalid Response. Please enter all fields to login")
        return redirect(url_for("login_page"))
    

    if not checkuser or not check_password_hash(checkuser.password, passcode):
        flash("Incorrect Login-Credentials. Please try again!")
        return redirect(url_for("login_page"))
    else:
        login_user(checkuser)
        return redirect(url_for("main_page"))


@app.route("/main", methods=["GET", "POST"])
@login_required
def main_page():
    """define mainpage"""
    user = current_user.username
    return flask.render_template("main.html", user=user)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def handle_logout():
    """handling logout"""
    logout_user()
    return redirect(url_for("login_page"))


app.run(debug=True)
