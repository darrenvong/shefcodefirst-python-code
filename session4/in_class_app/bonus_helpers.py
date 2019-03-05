"""
A collection of helper functions which contribute towards the solutions for some
of the bonus exercises in session 4.

In general, it is good practise to separate out code from app.py that aren't needed directly to
send back a response to the user, so that file doesn't become too cluttered! By separating out
functions used indirectly into its own file such as this, it also means your code can be re-used
across other files should the needs arise when the app becomes more sophisticated/complicated!

@author: Darren Vong
"""
import json

##################### Answer to bonus exercise 3 #####################
def load_shefcodefirst_python_members(file_path):
    """Given the `file_path` to the file containing a list of #ShefCodeFirst Python
    course members, this function loads them into a list and return such list back."""

    with open(file_path) as input_file:
        python_course_members = [member.strip() for member in input_file]
    return python_course_members


##################### Answer to bonus exercise 6 #####################
def load_weather_data(file_path):
    """Given the `file_path` to the file containing the weather data in JSON format,
    this function loads the data back into a dictionary and returns it."""

    with open(file_path) as weather_input:
        weather_data = json.load(weather_input)
    return weather_data
