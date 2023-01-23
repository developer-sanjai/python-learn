# function 


def greet(name):
    print(f"Hi{name}")
    print(f"How are you?{name}")
    print(f"Have a nice day!{name}")

run = True

while run:
    user_name = input("Enter your name: ")

    greet(name = user_name)

    user_choice = input("Do you want to continue?...(Y/N) ").lower()

    if user_choice == "n" :
        run = False
    