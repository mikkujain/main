import sys
import spy_status
from spy_details import Spy
import spy_friend
print("Welcome to SpyChat program")

# Module 1: Creating User Profile
# Now we have two options :-
# 1. Creating spy profile from default values.
# 2. Creating spy profile by taking input from the user.
print("Let's first create your profile\n")
profile_choice = input("Do you want to continue with the current settings? (y/n) ")

if profile_choice.upper() == 'Y':
	spy = Spy("Bond", "Mr.", 25, 4.8)
else :
	
	#validating the name
	name = input("What is your name? ")
	if name.isalpha() == False and name.isspace() !=False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	salutation = input("What should we call you? (Mr./ Mrs.) ")
	if salutation !='Mr.' and salutation !='Mrs.':
		print("invalid salutation")
		sys.exit(0)

	#validating the age
	age = int(input("how old are you? "))
	if age <= 12 or age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	rating = float(input("What is your rating? "))
	if rating > 4 and rating < 5:
		print("u are 3 star of spy")
	elif rating > 3 and rating < 4:
		print("u are 2 star of spy")
	elif rating > 2 and rating < 3:
		print("u are 1 star of spy")

	else:
		print("u are 0 star of spy")

	spy = Spy(name, salutation, age, rating)

# Printing spy details
print("\nHello %s %s " %(spy.salutation, spy.name))
print("We have successfully created your account")



# Module 2: Creating a menu
# To create menu, we will be defining the function start_chat()
def start_chat():
	show_menu = True
	while show_menu:
		print("\nYou can select from the operations")
		print("1. Add Friend\n 2. Add Status\n 3. Send Secret Message\n 4. Read Secret Message\n 5. Close application")
		menu_choice = int(input("What do you want to do: "))

		if menu_choice == 1:
			print("\nYou have chosen to add a friend")
			spy_friend.add_friend()
		elif menu_choice == 2:
			print("\nYou have chosen to add a status")
			spy.current_status_message = spy_status.add_status(spy.current_status_message)
		elif menu_choice == 3:
			print("\nYou have chosen to send message")
			spy_friend.send_message()
		elif menu_choice == 4:
			print("\nYou have chosen to read message")
			spy_friend.read_message()
			#print(current_chat)
		elif menu_choice == 5:
			print("\nYou have chosen to close the application")
			show_menu = False
		else:
			print("\nIncorrect choice")

spy_friend.load_friends()
spy.current_status_message = spy_status.load_status()
spy_friend.load_chat()
start_chat()
spy_friend.save_friends()
spy_status.save_status()
spy_friend.save_chat()

