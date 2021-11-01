print("Please choose an option from the list below")
#List of 5 options
Learn_Linux = 1
Learn_Pycharm = 2
Drive_a_car = 3
Have_Dinner = 4
Take_a_copy = 5
Exit = 0


print("1. Learn Linux")
print("2. Learn Pycharm")
print("3. Drive a car")
print("4. Have dinner")
print("5. Take a copy")
print("0. Exit")

'''
This program was supposed to be uploaded to the D2L with an individual team evaluation form per each member.


-2 [No comments in your program
    For the invalid options(other than 0-5), your program needs to display a different message.]

Use a lopp if you want this program to be executed repeatedly. extra point: 1 point out of 4 points
'''
command = int(input("Enter command"))

if command == 1:
    print("Please dont Learn Linux its extremely difficult.")

command = int(input("Enter command"))

if command == 2:
    print("Please Learn Pycharm it is pretty simple once you get the hang of it.")

command = int(input("Enter command"))

if command == 3:
    print("Learn how to Drive a car you dummy.")

command = int(input("Enter command"))

if command == 4:
    print("its time to have dinner.")

command = int(input("Enter command"))

if command == 5:
    print("Please dont take a copy of the teachers test scores.")

command = int(input("Enter command"))

if command == 0:
    print("exit now please")
