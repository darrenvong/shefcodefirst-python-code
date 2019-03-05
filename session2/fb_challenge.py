def check_identity(name):
    """Given a name as an argument, prints out who they are and
    what their role is on the #ShefCodeFirst Python course."""

    # Reading in a file into a list containing #ShefCodeFirst Python course members, so
    # either they are a student, an instructor or an ambassador
    with open("python_course_members.txt", encoding="utf-8") as input_file:
        python_course_members = [member.strip() for member in input_file]

    if name == "Charlotte" or name == "Lydia":
        print(f"{name} is an awesome #ShefCodeFirst ambassador! Go {name}!")

    if name in ["Darren", "Laura", "Adam", "Ashwani", "Katjuša"]:
        print(f"{name} is our awesome #ShefCodeFirst Python instructor! <3")

    if name in python_course_members:
        print(f"{name} is a student of #ShefCodeFirst's Python course! #WomenInTech")

check_identity("Laura")
