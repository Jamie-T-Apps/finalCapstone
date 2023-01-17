#=====importing libraries===========
'''This is the section where you will import libraries'''

import os
import datetime

#====Set Directory Path======

T21_FOLDER = os.path.dirname(__file__)
USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"

#=====Global Variables======

saved_user_logins = [] # stores [username, password] from users.txt
task_list = [] # stores [assigned to, title, description, created, due, completed?] from tasks.txt
current_user = "" # records the user name once login in

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# load user.txt info into saved_user_logins with username and pass combined 
# into a nested list so that the username and respective password are both stored together

with open(os.path.join(T21_FOLDER, USER_FILE), "r") as f:
    for line in f:
        line = line.strip() # .strip() removes line break
        line = line.split(", ")
        saved_user_logins.append(line)

# while loop assumes that login status is false until it is switched to true. Once true, while loop ends.

while True:
    try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user_logins in saved_user_logins:

                # assumes that [0] is always username and [1] is always password
                if username == user_logins[0] and password == user_logins[1]: 
                    print("Log in succesful!\n")
                    current_user = username
                    login_status = True
                    break
                else:
                    login_status = False
                
            if login_status:
                break
            else:
                print("Credentials not recognised. Try again.\n")
                continue
    except:
        print("Something went wrong. Try again.\n")


while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    if current_user == "admin": # s as an additional admin feature

        menu = input('''Select one of the following Options below:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        s - view statistics
                        e - Exit
                        : ''').lower()
    else:

        menu = input('''Select one of the following Options below:
                                r - Registering a user
                                a - Adding a task
                                va - View all tasks
                                vm - view my task
                                e - Exit
                                : ''').lower()

    if menu == 'r': # registering a new user by adding the input info to the users.txt file
        
        while True:
            if current_user != "admin": # admin permissions required to access this option
                print("\nOnly the admin can register users.\n") 
                break

            new_username = input("Enter a new username: ").lower()
            new_password = input("Create you new password: ").lower()
            confirm_password = input("Re-enter the password: ").lower()
            
            if new_password == confirm_password:
                with open(os.path.join(T21_FOLDER, USER_FILE), "a") as f:
                    f.write(f"\n{new_username}, {new_password}") # line break required to maintain file format
                print("New user created succesfully!\n")
                break
            
            else:
                print("Passwords didn't match. Try again.")
                continue


    elif menu == 'a': # add a task to tasks.txt based on user input
        print("\n")
        while True:

            task_username = input("Assign task to: ").lower()
            task_title = input("Assign task title: ").capitalize()
            task_description = input("Describe task as: ").capitalize()
            task_due_date = input("Assign task due date as DD Mon YYYY: ").title() # reliant on user for format
            date = datetime.datetime.now()
            task_created = date.strftime("%d %b %Y")

            # check that the action is assinged ot someone in the users.txt file
            # true as user in text file, false as user not in text file

            for user_and_pass in saved_user_logins:
                if task_username in user_and_pass:
                    user_found = True
                    break
                else:
                    user_found = False
            
            if user_found:
                with open(os.path.join(T21_FOLDER, TASK_FILE), "a") as f:
                    f.write(f"\n{task_username}, {task_title}, {task_description}, {task_created}, {task_due_date}, No")
                print(f"{task_title} has been assigned to {task_username}\n")
                break
            else:
                print("Username not found. Try again.")
                continue


    elif menu == 'va': # view all tasks with format similar to pdf doc

        with open(os.path.join(T21_FOLDER, TASK_FILE), "r") as f:
            for line in f:
                line = line.strip() # removes line break
                line = line.split(", ")
                task_list.append(line)

        print("\n")
        for task_data in task_list:
            print(f"*"*75)
            print(f"{'Task Title:':{20}}{task_data[1]:{20}}")
            print(f"{'Assigned to:':{20}}{task_data[0]:{20}}{'Created:':{20}}{task_data[3]}")
            print(f"{'Completed?:':{20}}{task_data[5]:{20}}{'Due By:':{20}}{task_data[4]}")
            print(f"{'Description:':{20}}")
            print(f"{'':{5}}{task_data[2]}")
            print("\n")

    elif menu == 'vm': # filters the tasks based on current_user value

        with open(os.path.join(T21_FOLDER, TASK_FILE), "r") as f:
            for line in f:
                line = line.strip() # removes line break
                line = line.split(", ")
                task_list.append(line)

        print(f"")
        for task_data in task_list:
            if current_user == task_data[0]:
                print(f"*"*75)
                print(f"{'Task Title:':{20}}{task_data[1]:{20}}")
                print(f"{'Assigned to:':{20}}{task_data[0]:{20}}{'Created:':{20}}{task_data[3]}")
                print(f"{'Completed?:':{20}}{task_data[5]:{20}}{'Due By:':{20}}{task_data[4]}")
                print(f"{'Description:':{20}}")
                print(f"{'':{5}}{task_data[2]}")
                print("\n")

    elif menu == 's':

        if current_user != "admin": # admin permissions required to access this option
                print("\nOnly the admin can view statistics.\n") 
                break

        task_count = 0
        user_count = 0
        
        # count lines and therefore tasks in task.txt
        with open(os.path.join(T21_FOLDER, TASK_FILE), "r") as f:
            for line in f:
                task_count += 1
        
        # count lines and therefore users in users.txt
        with open(os.path.join(T21_FOLDER, USER_FILE), "r") as f:
            for line in f:
                user_count += 1

        print("\n")
        print(f"*"*75)
        print(f"{'Number of Tasks':{20}}{task_count}")
        print(f"{'Number of Users':{20}}{user_count}")
        print("\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again\n")
