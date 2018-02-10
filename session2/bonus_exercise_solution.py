"""
Sample solution code for (mostly) the non-LPTHW bonus exercises in session 2.
@author: Darren Vong
"""

# Simplify the script by not using print(...) to show the questions.
# Questions are shown by passing it directly as an argument to the input
# function.
name = input("What's your name? ")
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, {name}, you're {age} year(s) old, {height} tall and {weight} heavy.")


# Assuming the user will only type in numbers, print out the sum of their age,
# height and weight.
total = int(age) + int(height) + int(weight)
print(f"The total of your age, height and weight is {total}")


# Make calling the add_two_numbers_from_args with exactly two arguments optional!
def add_two_number_from_args(number1=0, number2=0):
    answer = number1 + number2
    return answer

# Now all of the following call of the `add_two_number_from_args` function would be valid
add_two_number_from_args()
add_two_number_from_args(3)
add_two_number_from_args(6, 5)

# With keyword argument, you can even call the function without passing the arguments in
# order (by using the name of the arguments) as shown below:
add_two_number_from_args(number2=5, number1=6)


# Prints out "Hello world!" 10 times (or n times as required for the next part of
# the for loop exercise).
def print_hello_world(n):
    # _ is a Pythonic convention for variables in which we "don't care" about its
    # value (i.e. we won't use it)
    for _ in range(n):
        print("Hello world!")

print_hello_world(10)

# Write a function call guess_my_number that takes `answer` as an argument so when
# called, it continously asks the user for a number until they get it right.
def guess_my_number(answer):
    correct_guess = False
    while not correct_guess:
        guess = input("What number am I thinking of? ")
        if not guess.isdigit(): # makes sure the user is entering a number only
            print("Invalid input given - it must be a whole number!")
        elif int(guess) > answer:
            print("Nope, your guess was too high!")
        elif int(guess) < answer:
            print("Nope, your guess was too low!")
        else:
            print(f"Well done! You guessed {answer} correctly!")
            correct_guess = True

guess_my_number(62)
