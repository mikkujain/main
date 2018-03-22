import sys
import default

print("welcome to spychat program")
STATUS_MESSAGE=[]
def add_status(current_status_message):
    if (current_status_message !=None):
        print("Your current status is:" + current_status_message)

    else:
        print("U don't have any status message ")

    update_choice= input("Do u want to select older status (Y/N)?: ")
    if update_choice.upper()=='N':
        new_status_message=input("Enter a new status message")

        if len(new_status_message) > 0:
            updated_status_message=new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper()=='Y':
        if  STATUS_MESSAGE !=0:
            print("Go Ahead and select the status")
        if not any(STATUS_MESSAGE) :
            print("You can't select it becoz the list is empty")
            sys.exit(0)
        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + " " + STATUS_MESSAGE[i])

        message_selection = int(input("choose from older message"))
        if message_selection < len(STATUS_MESSAGE):
            updated_status_message=STATUS_MESSAGE[message_selection-1]

    return updated_status_message

def start_chat(spy_name,spy_age,spy_rating):
    current_status_message=None
    show_menu= True

    while show_menu:
        print("Choose the option which u wnat to do")
        menu_choice=int(input("1. Add a status update. \n 2. Close application"))
        if menu_choice==1:
            print("U have choosen to update a status")
            current_status_message=add_status(current_status_message)
        elif menu_choice==2:
            show_menu=False

choice = int(input("Enter 1 if u want to continuewith default settings "))
if choice == 1:
# user copy  the default value and put in.
    spy_name=default.spy_name
    spy_salutation=default.spy_salutation
    spy_age=default.spy_age
    spy_rating=default.spy_rating
    print("hello " + spy_salutation + spy_name)
    print("Your age is " + spy_age)
    print("your rating is " + spy_rating)
    if choice == 1:
        print(default.spy_rating1)
        #sys.exit(0)


else:
    #user given the name is correct or not
    spy_name=input("Enter your name")
    if spy_name.isalpha()== False:
        print("Name is invalid")
        print("Name should be lies in A to Z and a to z")
        sys.exit(0)

# check the salutation entered is correct or not
    spy_salutation=input("Enter your salutation (Mr. or Mrs.)")
    if not (spy_salutation == 'Mr.' or spy_salutation == 'Mrs.'):
        print("you are entred wrong input")
        sys.exit(0)

#validating the age of the spy_age
    spy_age=input("enter your age")
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

# to check the rating of user
    spy_rating=input("enteryour rating (A or B or C)")

    print("hello " + spy_salutation + spy_name)
    print("Your age is " + spy_age)
    print("your rating is " + spy_rating)
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

start_chat(spy_name,spy_age,spy_rating)
#print(current_status_message)
