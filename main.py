import sys
import default

print("welcome to spychat program")

choice = int(input("Enter 1 if u want to continuewith default settings "))
if choice == 1:

    spy_name=default.spy_name
    spy_salutation=default.spy_salutation
    spy_age=default.spy_age
    spy_rating=default.spy_rating
    #


else:
    #user given the name is correct or not
    spy_name=input("Enter your name")
    if spy_name.isalpha()== False:
        print("Name is invalid")
        print("Name should be lies in A to Z and a to z")
        sys.exit(0)
    #print("hello " + spy_salutation + spy_name)

    spy_salutation=input("Enter your salutation (Mr. or Mrs.)")
    if not (spy_salutation == 'Mr.' or spy_salutation == 'Mrs.'):
        print("you are entred wrong input")
        sys.exit(0)

    spy_age=input("enter your age")
    #validating the age of the spy_age
    if spy_age.isdigit() == False:
        print("number is invalid")
        print("number should be in digits only")
        sys.exit(0)
    elif int(spy_age) <= 12:
        print("Age is below 12")
        sys.exit(0)
    elif int(spy_age) >= 50:
        print("Age is above 50")
        sys.exit(0)

    #print("Your age is " + spy_age)

    spy_rating=input("enteryour rating (A or B or C)")
    #rating of the spy
    if spy_rating == 'A':
        print("you are 3 star spy")
    elif spy_rating == 'B':
        print("you are 2 star spy")
    elif spy_rating == 'C':
        print("you are 1 star spy")
    else:
        print("you have entered incorrect rating")
        sys.exit(0)
    #print("your rating is " + spy_rating)
print("hello " + spy_salutation + spy_name)
print("Your age is " + spy_age)
print("your rating is " + spy_rating)
if choice == 1:
    print(default.spy_rating1)
    sys.exit(0)
