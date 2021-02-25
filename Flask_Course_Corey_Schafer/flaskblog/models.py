# from flaskblog import db
# per evitare circular error usare una struttura package
from flaskblog import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# requisito per far funzionare FLask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # One-to-many relationship
        # backref : definisce una colonna nella tablela per fare il riferimento all'autore dei post
        # lazy True . indica che le info nel Db sono caricate solo su richiesta
    posts = db.relationship('Post', backref='author', lazy=True)


    # come l'object viene mostrato
    def __repr__(self):
        return f"User ('{self.username}', '{self.email}', '{self.image_file}') "


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # definisco l'id dell'user che scrive il post.
    # fa da riferimento allo user nella relazione tra tabelle. user.id è minuscolo per convenzione
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    # come l'object viene mostrato
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


db.create_all()





