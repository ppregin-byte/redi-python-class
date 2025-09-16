# Continuously loop until the user enters the empty string. 
while True:
    user_input = input("enter a string: ")
# if they just press the Enter or Return key, this results in an "empty string". 
# If they entered the empty string, end the loop.
    if user_input == "":
        print("Thanks for playing!")
        break
    else:
# Print out four different versions of the string using various string functions
        print(f"First letter capitalized: {user_input.capitalize()}")
        print(f"All lowercase: {user_input.lower()}")
        print(f"Title case: {user_input.title()}")
        print(f"All uppercase: {user_input.upper()}")