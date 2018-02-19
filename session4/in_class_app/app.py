from flask import Flask, render_template

app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return render_template("index.html")

# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
app.run(debug=True)
