"""
Sample solution code for the bonus exercises in session 4.

For completeness, the file also include the standard code we covered in class.
This means that to see the bonus exercise solutions working, you only need to run this file
as opposed to `app.py` (also included in this repository in case you want a simpler version
of the app to look at!) which only contains code we covered in class.

@author: Darren Vong
"""
from flask import Flask, render_template, request
from bonus_helpers import load_shefcodefirst_python_members, load_weather_data

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
    return render_template("hello.html", user=name)


@app.route("/feedback", methods=["POST"])
def get_feedback():
    # request.values is a dictionary holding any
    # POST request data not already part of the URL
    data = request.values

    return render_template("feedback.html", form_data=data)


##################### Answer to bonus exercise 1 #####################
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


##################### Answer to bonus exercise 4 #####################
# Notice that we can bind *multiple* URL patterns to a single function!
# In this case, we're doing this to prevent the app from crashing if the user visits this
# specific URL pattern with a slash at the end!
@app.route("/shefcodefirst-members")
@app.route("/shefcodefirst-members/")
def show_shefcodefirst_members():
    python_course_members = load_shefcodefirst_python_members("python_course_members.txt")
    return render_template("shefcodefirst_members.html", python_course_members=python_course_members)


##################### Answer to bonus exercise 5 #####################
# In hindsight... you could have completed the exercise with one function rather than three as
# suggested when I first wrote it if you define the URL pattern more cleverly like the following:
@app.route("/shefcodefirst-members/<role>")
def show_specific_shefcodefirst_members(role):
    # The main lists of people to filter the bigger members list against...
    ambassadors = ["Lydia", "Charlotte"]
    instructors = ["Darren", "Laura", "Ashwani", "Adam", "Katjuša"]

    # Ensures "role" is in all lower-cased letter before we perform the comparison below...
    role = role.lower()

    if role == "students":
        python_course_members = [student for student in
                                 load_shefcodefirst_python_members("python_course_members.txt")
                                 if student not in ambassadors and student not in instructors]
    elif role == "ambassadors":
        python_course_members = ambassadors
    elif role == "instructors":
        python_course_members = instructors
    else:
        python_course_members = []

    return render_template("shefcodefirst_members.html",
                           python_course_members=python_course_members, role=role)


##################### Answer to bonus exercise 7, 8 #####################
@app.route("/weather/<location>")
def show_weather(location):
    location = location.capitalize()
    loc_specific_weather_data = {}
    for weather_data_dict in load_weather_data("../weather_data.json")["data"]:
        if weather_data_dict["name"] == location:
            loc_specific_weather_data = weather_data_dict
            # Found the specific location's weather data, so we can safely break out of loop early
            break

    if loc_specific_weather_data:
        # dictionary is only filled up properly if the location is available in weather data file
        return render_template("weather.html", location=loc_specific_weather_data["name"],
                               temperature=loc_specific_weather_data["temperature"],
                               description=loc_specific_weather_data["description"])
    else:
        return render_template("weather.html"), 404

# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
app.run(debug=True)
