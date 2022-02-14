from flask import Flask, render_template, redirect, url_for, Blueprint
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date, datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddgibDHUDQ27482374829DIFHOSCOS37402'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    Name = db.Column(db.String(250), nullable=False)
    Message = db.Column(db.Text, nullable=False)
# db.create_all()

##WTForm
class CreateForm(FlaskForm):
  name = StringField("Your Name", validators=[DataRequired()])
  email = StringField("Your Email", validators=[DataRequired()])
  message = StringField("Your message", validators=[DataRequired()])
  submit = SubmitField("Submit")


@app.route('/')
def home():
  return render_template("index.html")

@app.route('/resume')
def resume():
  return render_template("resume.html")

@app.route('/about', methods=["GET", "POST"])
def about():
    form = CreateForm()
    return render_template("about.html", form=form)

@app.route('/portfolio')
def portfolio():
  return render_template("portfolio.html")

if (__name__) == "__main__":
  app.run(debug=True)
