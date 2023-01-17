# ============= IMPORTS ==============

import os
import datetime


# ============= GLOBAL VARIABLES ==============

login_required = True
current_user = ""

# ============= FUNCTIONS ==============

def get_data(file, method):
    # load data from either users or text into a list variable
    temp_data = []
    with open(os.path.join(os.path.dirname(__file__), file), method) as f:
        i = 1 # i as the line number for psuedo ID
        for line in f:
            line = line.strip() # .strip() removes the line break
            line = line.split(", ") # split() turns info into a list
            line.insert(0, i)
            temp_data.append(line)
            i += 1
    return temp_data

def write_data(file, method, data):
    # data must be in list format
    with open(os.path.join(os.path.dirname(__file__), file), method) as f:
        for line in data:
            line = (", ").join(line) # turns list into format required by .txt files
            f.write(f"{line}\n")
    return print(f"\n{file} updated\n")

def get_logins():
    # load data from users.txt as dictionary
    temp_logins= {}
    for user_and_pass in get_data("user.txt", "r"):
        # for user_and_pass [0] is line num, [1] is username, [2] is password
        temp_logins[user_and_pass[1]] = user_and_pass[2] 
    return temp_logins

def get_list(file):
    # load data from tasks.txt
    # and retun as an indexed list
    temp_task_list = []
    for tasks in get_data(file, "r"):
        temp_task_list.append(tasks)
    return temp_task_list
        
def valid_login(username, password):
    # checks username and password combination against dictionary from users.txt
    if get_logins()[username] == password:
        return True
    else:
        return False
 
def user_is_admin():
    # checks to see whether the current user is the admin
    if current_user == "admin":
        return True
    else:
        return False

def show_menu_options():
    # shows the user a menu depending on their account, and returns their choice of options
    if user_is_admin():
        menu = input('''Select one of the following Options below:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        s - view statistics
                        gr - generate report
                        e - Exit
                        : ''').lower()
        return menu
    else:
        menu = input('''Select one of the following Options below:
                                a - Adding a task
                                va - View all tasks
                                vm - view my task
                                e - Exit
                                : ''').lower()
        return menu

def reg_user(username, password):
    # add username and password to users.txt file
    temp_list = [[username, password]]
    write_data("user.txt", "a", temp_list) # write_data requires list to be nested in a list
    return print(f"\n{username} added to login file.\n")

def is_new_user(check_username):
    # check to see if username entered exists in dictionary for user.txt
    if check_username in get_logins():
        return False
    else:
        return True

def add_task(task_username):
    # adds task info to tasks.txt based on user input
    # should only be called if is_new_user() check returns true
    # is_new_user check run first to reduce amount of user input if username does not exist
    task_title = input("Assign task title: ").capitalize()
    task_description = input("Describe task as: ").capitalize()
    task_due_date = input("Assign task due date as DD Mon YYYY: ").title() # reliant on user for format
    date = datetime.datetime.now()
    task_created = date.strftime("%d %b %Y")
    temp_list = [list(((task_username, task_title, task_description, task_created, task_due_date, "No")))]
    write_data("tasks.txt", "a", temp_list)
    
    return print(f"\n{task_title} added to task list\n")

def view_all():
    # prints all the tasks in tasks.txt
    for task_data in get_data("tasks.txt", "r"):
        print(f"*"*75)
        print(f"{'Task ID:':{20}}{task_data[0]:{20}}")
        print(f"{'Task Title:':{20}}{task_data[2]}")
        print(f"{'Assigned to:':{20}}{task_data[1]:{20}}{'Created:':{20}}{task_data[4]}")
        print(f"{'Completed?:':{20}}{task_data[6]:{20}}{'Due By:':{20}}{task_data[5]}")
        print(f"{'Description:':{20}}")
        print(f"{'':{5}}{task_data[3]}")
        print("\n")
    
    return edit_task(id = input("Enter the ID number of the task you would like to edit: "))

def view_mine():
    # prints all the tasks in tasks.txt that are assinged to the current user
    for task_data in get_data("tasks.txt", "r"):
        if current_user == task_data[1]:
            print(f"*"*75)
            print(f"{'Task ID:':{20}}{task_data[0]:{20}}")
            print(f"{'Task Title:':{20}}{task_data[2]}")
            print(f"{'Assigned to:':{20}}{task_data[1]:{20}}{'Created:':{20}}{task_data[4]}")
            print(f"{'Completed?:':{20}}{task_data[6]:{20}}{'Due By:':{20}}{task_data[5]}")
            print(f"{'Description:':{20}}")
            print(f"{'':{5}}{task_data[3]}")
            print("\n")

    return edit_task(id = input("Enter the ID number of the task you would like to edit: "))

def count_items(file, items):
    # counts the number of lines in specified file
    # items as the number ot {items} to be printed
    item_count = 0
    for line in get_data(file, "r"):
        item_count += 1
    return print(f"Number of {items}: {item_count}")

def generate_user_report():

    temp_users = get_data("user.txt", "r")
    temp_tasks = get_data("tasks.txt", "r")
    current_date = datetime.datetime.now()
    temp_list = ""

    # total users
    total_users = len(temp_users)

    # total tasks
    total_tasks = len(temp_tasks)

    # stats per user
    for user_data in temp_users: # user_data[0] is the username
        user = user_data[1]
        user_task_count = 0
        user_completed_tasks = 0
        user_open_tasks = 0
        user_overdue_tasks = 0

        for task_data in temp_tasks: # task_data[0] is the username for the task
            if user == task_data[1]:
                user_task_count += 1
                
                if task_data[6] == "Yes":
                    user_completed_tasks += 1
                else:
                    user_open_tasks += 1

                    task_due_date = datetime.datetime.strptime(task_data[5], "%d %b %Y")

                    if task_due_date <= current_date:
                        user_overdue_tasks += 1

        if user_task_count == 0:
            user_percentage_total, user_percentage_complete, user_percentage_open, user_percentage_overdue = 0.0, 0.0, 0.0 ,0.0
        else:
            user_percentage_total = round(user_task_count / total_tasks * 100, 2)
            user_percentage_complete = round(user_completed_tasks / user_task_count * 100, 2)
            user_percentage_open = round(user_open_tasks / user_task_count * 100, 2)
            user_percentage_overdue = round(user_overdue_tasks / user_task_count * 100, 2)
        
        temp_line = (f"User: {user}\t\tTasks: {user_task_count}\t\tCompleted: {user_completed_tasks}\t\t"
                    f"Open: {user_open_tasks}\t\tOverdue: {user_overdue_tasks}\t\t"
                    f"% of total tasks: {user_percentage_total}\t\t% of tasks complete: {user_percentage_complete}\t\t"
                    f"% of tasks open: {user_percentage_open}\t\t% of tasks overdue: {user_percentage_overdue}\n")
        temp_list += temp_line

        

    temp_list = [ [f"Total Users: {total_users}"], [f"Total Tasks: {total_tasks}"], [temp_list] ]   
    
    write_data("user_overview.txt", "w", temp_list) 

    return
 

def generate_task_report():
    # generates text doc containing report info for tasks.txt

    temp_tasks = get_data("tasks.txt", "r")
    current_date = datetime.datetime.now()

    # total tasks
    total_tasks = len(temp_tasks)
    
    # total completed, open, and overdue (overdue count only applies to open tasks)
    completed_tasks = 0
    open_tasks = 0
    overdue_tasks = 0

    for task_data in temp_tasks:
        if task_data[6] == "Yes":
            completed_tasks += 1
        else:
            open_tasks += 1
            task_due_date = datetime.datetime.strptime(task_data[5], "%d %b %Y")
           
            if task_due_date <= current_date:
                overdue_tasks += 1

    # percentage incomplete
    percentage_incomplete = round((open_tasks / total_tasks) * 100, 2)

    # percentage incomplete and overdue
    percentage_overdue = round((overdue_tasks / total_tasks) * 100, 2)
    
    # write data to text file
    temp_list = [ [f"Total Tasks:\t\t{total_tasks}\nOverdue tasks:\t\t{overdue_tasks}\nOpen Tasks:\t\t{open_tasks}\n"
                    f"Completed Tasks:\t{completed_tasks}\n% Incomplete:\t\t{percentage_incomplete}\n% Overdue:\t\t{percentage_overdue}"] ]
    
    write_data("task_overview.txt", "w", temp_list)
        
    return

def show_stats(area):
    # prints either user_overview.txt or task_overview.txt in console

    if area == "users":
        temp_list = get_list("user_overview.txt")
    elif area == "tasks":
        temp_list = get_list("task_overview.txt")
    else:
        print("*"*75)
        print("No stats found")
        return print("")
    
    print("*"*75)
    for line in temp_list:
        print(line[1]) # line[0] is the index applied to the data and is not required for this function
    return print("")

def edit_task(id):
    # edit task function that overwrites data in tasks.txt
    # note that the data passed to the write data function must be in nested list format
    # and must not include the numberical ID that is assinged as part of the get_data fucntion

    if id == "-1":
        return print("\nExiting edit function.\n")
    else:
        while True:
            try:
                temp_tasks = get_data("tasks.txt", "r")
                id = int(id)
                for task_data in temp_tasks:
                    task_title = task_data[2]
                    if int(task_data[0]) == id:
                        if task_data[6] == "Yes":
                            print(f"\nTask {id} - {task_title} cannot be edited as it is complete.\n")
                            return edit_task(id = input(f"Try entering an ID number between 1 and {len(temp_tasks)}, or -1 to exit: "))
                        else:
                        # in  task_date [1]=username, [6]=completed, [5]=due date
                            match input("What would you like to edit? (1 = change username, 5=change due date, 6=mark as complete, -1=exit): "): 
                                case "1":
                                    old_username = task_data[1]
                                    new_username =  input(f"Change username from {old_username} to: ")
                                    
                                    if is_new_user(new_username):
                                        print(f"{new_username} is not a recognised username.\n")
                                        continue
                                    else:
                                        task_data[1] = new_username.lower()
                                        write_data("tasks.txt", "w", list(strip_id(temp_tasks)))
                                        return print(f"Task {id} - {task_title} username changed from {old_username}"
                                                    f" to {new_username}\n")
                                case "5":
                                    old_due_date = task_data[5]
                                    new_due_date = input(f"Change due date from {old_due_date} to (use DD Mon YYYY format): ")
                                    if is_valid_date_format(new_due_date):
                                        task_data[5] = new_due_date
                                        write_data("tasks.txt", "w", list(strip_id(temp_tasks)))
                                        return print(f"Task {id} - {task_title} due date changed from {old_due_date}"
                                                    f" to {new_due_date}\n")
                                    else:
                                        print(f"{new_due_date} is not in DD Mon YYYY format.\n")
                                        continue
                                case "6":
                                    task_data[6] = "Yes"
                                    write_data("tasks.txt", "w", list(strip_id(temp_tasks)))
                                    return print(f"Task {id} - {task_title} completion status changed from No"
                                                    f" to Yes\n")
                                case "-1":
                                    return print("\n")
            except:
                return edit_task(id = input(f"Try entering an ID number between 1 and {len(temp_tasks)}, or -1 to exit: "))

def strip_id(data):
    # strips the id number that is added in get_data function
    # used for edit tasks prior to calling write_data function
    for line in data:
        line.pop(0)
    return data

def is_valid_date_format(data):
    # checks that the info entered is in the DD Mon YYYY format required to maintain integrity of data in txt files
    res = bool(datetime.datetime.strptime(data, "%d %b %Y"))
    return res

# ============= LOGIC ==============

# check if user is logged in, and request username and password if not

while True:
    try:
        if login_required:
            username = input("Enter your username: ").lower()
            password = input("Enter your password: ").lower()

            if valid_login(username, password):
                print(f"\nWelcome {username}. You are now logged in.\n")
                current_user = username
                login_required = False
            else:
                print("\nCredentials not recognise. Try again. \n")
                continue
        break
    except:
        print("There's an issue with the login logic")

# show user the options and continously loop through this until logout

while True:
    try:
        match show_menu_options():

            case "r":
                if user_is_admin():
                    new_username = input("Enter a new username: ")

                    if is_new_user(new_username):
                        new_password = input("Enter password: ")
                        confirm_password = input("Confirm password: ")

                        if new_password == confirm_password:
                            reg_user(new_username, new_password)
                        else:
                            print("\nPasswords don't match.\n")
                            continue
                    else:
                        print("\nUsername already exists.\n")
                        continue

                else:
                    print("\nOnly an admin can register new users.\n")
                    continue

            case "a":

                task_username = input("Assign task to: ").lower()
                
                if is_new_user(task_username):
                    print("\nUsername not found. Try again.\n")
                    continue
                else:
                    add_task(task_username)

            case "va":

                view_all()

            case "vm":

                view_mine()

            case "s":

                if user_is_admin():
                    show_stats("tasks")
                    show_stats("users")
                else:
                    print("\nOnly an admin can view stats.\n")
                    continue

            case "gr": 

                generate_task_report()
                generate_user_report()

            case "e":

                print("\nGoodbye!!!\n")
                exit()

    except Exception:
        print("There's an issue with the menu selection logic")