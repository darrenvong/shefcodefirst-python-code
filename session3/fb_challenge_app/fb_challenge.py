def check_identity(name):
    """Given a name as an argument, prints out who they are and
    what their role is on the #ShefCodeFirst Python course."""

    # Reading in a file into a list containing #ShefCodeFirst Python course members, so
    # either they are a student, an instructor or an ambassador
    with open("python_course_members.txt") as input_file:
        python_course_members = [member.strip() for member in input_file]

    single_role_members = ["Darren", "Laura", "Adam", "Ashwani", "Katjuša", "Lydia"]

    # Message variable needed to hold the message built so far as we don't know how many
    # roles the name given has until it has been run through the logic below. 
    message = ""

    name = name.capitalize() # Ensures the first letter of name is in upper case

    if name == "Charlotte" or name == "Lydia":
        message = f"{name} is an awesome #ShefCodeFirst ambassador! Go {name}!"
    elif name in ["Darren", "Laura", "Adam", "Ashwani", "Katjuša"]:
        message = f"{name} is our awesome #ShefCodeFirst Python instructor! <3"

    if name in python_course_members and name not in single_role_members:
        message += f" {name} is a student of #ShefCodeFirst's Python course! #WomenInTech"
    elif message == "":
        message = f"We don't know who {name} is! Maybe you typed in the wrong name?"

    return message
