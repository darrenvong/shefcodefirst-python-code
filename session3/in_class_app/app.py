# To use functions from a library you installed via pip, you have to import them first.
# Importing functions using the "from x import a, b, c" style allows you to use
# the function directly. In other words, you can write a(), b() instead of x.a(), x.b() each time
# you want to call the imported functions.
from flask import Flask, render_template

# This creates the all important Flask application which will give you the ability
# to serve (respond) web pages back to your users based on the web address (URL) they
# typed in the browser
app = Flask("my_first_app")

# @app.route(...) is a "magic function" (decorator) which upgrades a standard Python
# function to one which can handle requests from the user when they are visiting this route.
# The full route is most likely going to be "localhost:5000" when running the app locally
# on your laptop.
@app.route("/")
def say_hello():
    return "Hello world!"

    # As we moved through the slides, we replaced the line above with the line
    # below. Comment out the line above and uncomment the line below to see the
    # difference when visiting "localhost:5000" (you should see a larger "Hello world!")

    # return render_template("index.html")

# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
app.run(debug=True)
