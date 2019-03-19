from flask import Flask, request
import praw

app = Flask(__name__)

client_id = "xxx"
client_secret = "xxx"
username = "xxx"
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri='http://localhost:5000/redditCallback',
                     user_agent=f"Python:{client_id}:v1 (by /u/{username}")


@app.route("/")
def index():
    return f"<a href='{reddit.auth.url(['identity', 'read'], 'some_secret')}'>Click this link to authorise my app</a>"

@app.route("/callback")
def reddit_callback():
    code = request.values.get("code")
    refresh_token = reddit.auth.authorize(code)
    return f"{reddit.user.me()} logged in."

@app.route("/something")
def some_other_reddit_feature():
    for submission in reddit.front.hot(limit=10):
        print(submission)
    return "all ok"

app.run(debug=True)
