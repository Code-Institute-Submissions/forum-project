import os
from datetime import datetime
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
print(os.environ.get("MONGO_URI"))

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    catogories = list(mongo.db.catogories.find())
    topics = list(mongo.db.Topics.find())
    return render_template("home.html", topics=topics, catogories=catogories)


@app.route("/catogory/<catogory_id>")
def catogory(catogory_id):
    catogories = list(mongo.db.catogories.find({"_id": ObjectId(catogory_id)}))
    topics = list(mongo.db.Topics.find())
    return render_template("catogory.html", catogory=catogories, topics=topics)


@app.route("/current_topic/<topic_id>", methods=['GET', 'POST'])
def current_topic(topic_id):
    if request.method == 'POST':
        if session['user']:
            now = datetime.now()
            comment = {
                "comment_text": request.form.get("new_comment"),
                "user_id": session['user'],
                "Topics_id": ObjectId(topic_id),
                "last_edited": now
            }
            mongo.db.comments.insert_one(comment)
            mongo.db.Topics.update(
                {"_id": ObjectId(topic_id)},
                {"$set": {"last_edited": now},
                 "$inc": {"posts": 1}})
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    users = list(mongo.db.users.find())
    current_topic_id = mongo.db.Topics.find({"_id": ObjectId(topic_id)})
    comments = mongo.db.comments.find({"Topics_id": ObjectId(topic_id)})
    return render_template('topic.html', topicinfo=current_topic_id,
                           comments=comments, users=users)


@app.route('/create_topic', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        # checks if topic doesnt already exists
        existing_topic = mongo.db.Topics.find_one(
            {"topic_title": request.form.get("topic_title")})

        if existing_topic:
            flash("Topic already exists")
            return redirect(url_for("create_topic"))
        # Gets current time +0.00
        now = datetime.now()

        new_topic = {
            "catogory": request.form.get("catogory"),
            "topic_title": request.form.get("topic_title"),
            "username": session['user'],
            "last_edited": now,
            "posts": 1
        }

        mongo.db.Topics.insert_one(new_topic)
        # gets topic object ID
        objectid = mongo.db.Topics.find_one(new_topic)['_id']
        new_comment = {
            "comment_text": request.form.get("new_comment"),
            "user_id": session['user'],
            "Topics_id": ObjectId(objectid),
            "last_edited": now
        }

        mongo.db.comments.insert_one(new_comment)
        return redirect(url_for('home'))
    catogories = mongo.db.catogories.find()
    return render_template('create_topic.html', catogories=catogories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_image": request.form.get("user_image")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                                   "home", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    if session["user"]:
        username = mongo.db.users.find_one(
             {"username": session["user"]})["username"]
        print(username)
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
