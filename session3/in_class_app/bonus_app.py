from flask import Flask, render_template

app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return render_template("index.html")

##################### Answer to bonus exercise 1 #####################
@app.route("/<name>")
def say_hello_to(name):
    return render_template("index.html", user=name)

##################### Answer to bonus exercise 2, 3 #####################
# In variable route patterns, you can also apply a converter to the captured variable.
# So, in this case, both number1 and number2 will be converted to integers.
# If the user enters anything other than whole numbers, then this route pattern won't
# be matched.
@app.route("/<int:number1>/<int:number2>")
def show_two_numbers_total(number1, number2):
    total = number1 + number2
    return render_template("total.html", number1=number1, number2=number2, total=total)

    # The following will suffice for bonus exercise 2
    # return f"The total of {number1} and {number2} is {total}"

##################### Answer to bonus exercise 4 #####################
# Since Flask matches the same family of URL pattern from top to bottom, if the above
# is not matched, then the user must have entered a non-numerical value which is
# matched by this two-level catch-all fallback pattern.
@app.route("/<number1>/<number2>")
def two_variable_pattern_page(number1, number2):
    total = "Not a number"
    return render_template("total.html", number1=number1, number2=number2, total=total)

##################### Answer to bonus exercise 5 #####################
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404

# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
app.run(debug=True)
