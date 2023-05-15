from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    age = db.Column(db.Integer)

@app.route("/")
def index():
    users = User.query.all()
    return render_template("users.html", users=users)

print("whooo")
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    print(f"Got to add_user with request: {request.method}")
    if request.method == "POST":
        print(request)
        username = request.form.get('username', "Kashy")
        print(f"Parsed email data: {username}")
        email = request.form.get('email', "kashy@yhsak.io")
        print(f"Parsed age data: {email}")
        age = request.form.get('age', 27)
        print(f"Parsed username data: {age}")
        print("Creating user object")
        user = User(username=username, email=email, age=age)
        db.session.add(user)
        db.session.commit()
        print("Committing user object to database")
        return redirect(url_for("index"))
    else:
        return render_template("add_user.html")
    
@app.route("/delete_users", methods=["POST", "DELETE"])
def delete_users():
    db.drop_all()
    db.create_all()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
