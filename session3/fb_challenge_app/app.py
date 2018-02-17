from flask import Flask
from fb_challenge import check_identity

app = Flask(__name__)

@app.route("/")
def index():
    """Fallback root path request handler so that the user doesn't
    get greeted with a nasty "Not Found" page"""
    return "It works!"

# For more of what <name> means in the route pattern, see this help doc from Flask here:
# http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules. One thing to note:
# the argument names in the function has to match those used in the pattern!
@app.route("/ambassador/<name>")
def get_ambassador(name):
    name = name.capitalize() # Makes sure only first letter of name is in upper case
    return check_identity(name)

@app.route("/instructor/<name>")
def get_instructors(name):
    name = name.capitalize()
    return check_identity(name)

    app.run(debug=True)
