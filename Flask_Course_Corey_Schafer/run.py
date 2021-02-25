# from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy
#
# ## from models import User, Post
# # qui si presenta un circula loop. xche viene caricato il moduilo modules al cui interno
# # si richiede che venga caricato da questo file 'db'; ma 'db' non è ancora stato
# # letto da python.
# # Ma qui c'è anche un altro problema; infatti python riporta l'errore
# # che non conosce User e non su 'db'; questo perchè la prima linea di codice
# # in modules è l'import di questo file e ancora prima dio leggere 'db' cerca User
# # che però non ha ancora letto nel modulo 'modules'
# ##Soluzione
# # 1. rinominare 'flaskblog' nell'import statement nel modulo 'modules'
# #    con '__main__' e non far partire il flask blog direttamente  ma usare unba
# #    struttura package
# # 2. spostare lo statement di import di 'modules' dopo la ceazione
# #    dell'oistanza 'db'
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
#
# # Inizialization
# db = SQLAlchemy(app)
# from models import User, Post
#
#
#
#
#
# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]
#
#
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)
#
#
# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')
#
#
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
#
#
#
## sposto la parte delle route in aun altro file e
## rinomino questo come run.py lasciando solo il codice qui sotto
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)