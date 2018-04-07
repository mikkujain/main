import sys
import spy_friend
from spy_details import Spy, chatMessage
import csv

STATUS_MESSAGE = []
def add_status(current_status_message):
    
    #print the current status message
    if current_status_message == None:
        print("You do not have any current status")
        print("You need to add a status")
        message=input("Enter a status")
        if len(message)>0:
            updated_status_message=message
            STATUS_MESSAGE.append(updated_status_message)
    else:
        print("Your current status is " + current_status_message)

    #Ask the user if wants to choose from the older status or want to add a new status
    update_choice = input("Do you want to select from older status(y/n)?: ")
    
    #if the user wants to add a new status message, input the new status message
    if update_choice.upper() == 'N':
        new_status_message = input("Enter new status message: ")
        #Validate if the status message is not empty and append it to the list holding all the status messages
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper() == 'Y':
        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + " " + STATUS_MESSAGE[i])

        message_selection = int(input("Choose from the older message"))
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]

    return updated_status_message

def load_status():
    read_object = open("status.csv", 'rb')
    reader = csv.reader(read_object)
    for row in reader:
        STATUS_MESSAGE.append(row[0])
    read_object.close()
    if len(STATUS_MESSAGE) > 0:
        return STATUS_MESSAGE[-1]
    else:
        return None

def save_status():
    write_object = open("status.csv",'wb')
    writer = csv.writer(write_object)
    for i in range(len(STATUS_MESSAGE)):
        writer.writerow([STATUS_MESSAGE[i]])
    write_object.close()


    
