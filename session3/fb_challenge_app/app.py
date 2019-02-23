from flask import Flask
from fb_challenge import check_identity

app = Flask(__name__)

@app.route("/")
def index():
    """Fallback root path request handler so that the user doesn't
    get greeted with a nasty "Not Found" page"""
    return "It works!"

# For more of what <name> means in the route pattern, see this help doc from Flask here:
# http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules. One thing to note:
# the argument names in the function has to match those used in the pattern!
@app.route("/ambassadors/<name>")
def get_ambassador(name):
    return check_identity(name)

@app.route("/instructors/<name>")
def get_instructor(name):
    return check_identity(name)

@app.route("/students/<name>")
def get_student(name):
    return check_identity(name)

    app.run(debug=True)
