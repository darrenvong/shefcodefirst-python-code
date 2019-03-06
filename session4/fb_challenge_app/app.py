from flask import Flask, render_template, request, redirect, session, url_for
from secrets import token_bytes

app = Flask(__name__)

# A secret key is needed to use sessions. A session is what allows us to store
# information between each (web) request made by a particular user (such as logged
# in status on a system), since by default (and by design), each request is
# independent from each other and so aren't aware of each other.
# To generate secret key tokens, we can use the handy "token_bytes" function coming
# from the secrets library which comes with our Python installation
# (but not by default, so it needs to be imported).
app.secret_key = token_bytes()


@app.route("/")
def index():
    return render_template("index.html", bad_access=session.get("bad_access"),
                           message=session.get("message"))

@app.route("/home")
def home():
    user_info = request.values
    if user_info:  # Check that you're not directly trying to access the page!
        # Check that you've typed in a name and a password...
        if user_info.get("name") and user_info.get("password"):
            update_session(bad_access=False, message="")
            return render_template("content.html")
        else:
            update_session(bad_access=True,
                           message="No username or password provided! Please try again!")
            # The url_for function takes the name of a function we've defined in this file,
            # and returns the relative URL to our application. The redirect function then
            # takes this URL and redirects the user to the page.
            return redirect(url_for("index"))
    else:
        update_session(bad_access=True,
                       message="You need to log in first before you can access the course content!")
        return redirect(url_for("index"))

def update_session(bad_access=False, message=""):
    session["bad_access"] = bad_access
    session["message"] = message

app.run(debug=True)
