import os
from flask import (Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print(os.environ.get("MONGO_URI"))

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    topics = mongo.db.Topics.find()
    return render_template("home.html", topics=topics)

@app.route("/current_topic/<topic_id>")
def current_topic(topic_id):
    topic_id = mongo.db.Topics.find({"_id": ObjectId(topic_id)})
    return render_template('topic.html', topicinfo=topic_id)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
