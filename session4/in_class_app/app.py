from flask import Flask, render_template, request

app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return render_template("index.html")

# Notice that the function name is different from above!
# (say_hello_to rather than *just* say_hello!)
@app.route("/<name>")
def say_hello_to(name):
    # "name" in the function's argument HAS TO match that defined
    # in the <name> variable URL pattern
    return render_template("index.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
    # request.values is a dictionary holding any
    # POST request data not already part of the URL
    data = request.values

    return render_template("feedback.html", form_data=data)

# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
app.run(debug=True)
