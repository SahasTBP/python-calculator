import os
import sys
# Welcome message
def start():
    print("Welcome to the CALCUALTOR ! ")
    print("What do you want to do ? ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("----------------------------")


start()

def exit_choice():
    print("1. RESTART")
    print("2. EXIT")
    quit_choice = int(input(">> "))
    if quit_choice == 1:
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif quit_choice == 2:
        exit(0)

# Functions
def ask_numbers():
    ask_numbers.num1 = float(input("Number 1: "))
    ask_numbers.num2 = float(input("Number 2: "))
def add():
    ask_numbers()
    answer = ask_numbers.num1 + ask_numbers.num2
    print("Answer is: " + str(answer))
    exit_choice()

def subtract():
    ask_numbers()
    answer = ask_numbers.num1 - ask_numbers.num2
    print("Answer is: " + str(answer))
    exit_choice()

def multiply():
    ask_numbers()
    answer = ask_numbers.num1 * ask_numbers.num2
    print("Answer is: " + str(answer))
    exit_choice()

def divide():
    ask_numbers()
    answer = ask_numbers.num1 / ask_numbers.num2
    print("Answer is: " + str(answer))
    exit_choice()

# choice
def ask_choice():
    choice = int(input(">> "))
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        print("Exitting...")
        exit(0)
    else:
        ask_choice()


ask_choice()


# Exit
input("Press ENTER to exit...")
