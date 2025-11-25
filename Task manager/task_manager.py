# ===== Importing external modules ===========
'''This is the section where you will import modules'''
import os
import getpass
import textwrap
from datetime import datetime, date
from colorama import Fore, init
init(autoreset = True)


def load_users():
    '''
    Read users.txt and store in a dictionary

    Returns:
        users_dict (dictionary): usernames and passwords, key-value
    '''
    users_dict = {}
    try:
        with open("user.txt", "r", encoding= "utf-8") as file:
            for line_num, line in enumerate(file, 1):
                data = line.strip()
                if not data:  # Skip empty lines
                    continue
                parts = data.split(", ")

                # Validate line format
                if len(parts) == 2:
                    username, password = parts
                    if username and password:
                        users_dict[username] = password
                    else:
                        print(f"{Fore.RED}Line {line_num} missing data")
                        continue
                else:
                    print(f"{Fore.RED}Invalid format on line {line_num}")
                    continue

    except FileNotFoundError:
        if not users_dict:
            print("No users found. Creating with default admin.")
            save_users({"admin": "adm1n"})
            return {"admin": "adm1n"}

    return users_dict


def save_users(users_dict):
    '''
    Write new users to user text file

    Arg:
        user_dict (dictionary): usernames and passwords, key-value
    '''
    try:
        with open("user.txt", "w", encoding= "utf-8") as file:
            for username, password in users_dict.items():
                file.write(f"{username.strip()}, {password.strip()}\n")

    except FileNotFoundError:
        print(f"{Fore.RED}Error writing to file.")


def load_tasks():
    '''
    This function will read tasks from a text file and store in a list
    '''
    tasks = []
    try:
        with open("tasks.txt", "r", encoding= "utf-8") as file:
            for line_num, line in enumerate(file, 1):
                data = line.strip()
                if not data:  # Skip empty lines
                    continue

                parts = data.split(", ")
                if len(parts) != 6:  # Make sure all fields have data
                    print(Fore.RED + f"Invalid: line {line_num} ")
                    continue

                tasks.append({
                    "username": parts[0],
                    "title": parts[1],
                    "description": parts[2],
                    "date_assigned": parts[3],
                    "due_date": parts[4],
                    "completed": parts[5]
                    })
        return tasks
    except FileNotFoundError:
        print(f"{Fore.RED}Error reading file: try using empty list.")
        return []


def save_tasks(tasks):
    '''
    This function will write to tasks.txt file
    
    Arg:
        tasks (list): list of task dictionaries
    '''
    try:
        with open("tasks.txt", "w", encoding= "utf-8") as file:
            for task in tasks:
                line = (f"{task['username']}, {task['title']}, "
                        f"{task['description']}, {task['date_assigned']}, "
                        f"{task['due_date']}, {task['completed']}\n")
                file.write(line)
    except OSError as e:
        print(f"{Fore.RED}Error writing to file: tasks.txt {e}")


def print_header(title="", current_user=""):
    '''
    This function will print the header with the title and current user

    Args:
        title (str): Title of the section
        current_user (str): Username of current user
    '''
    header_str = f"TASK MANAGER: {title}"
    print("="*50)
    print(f"|{header_str:^{50-2}}|")  # Center header
    print("-"*50)
    if current_user:
        print(f"Current user: {current_user}")
        print("-" * 25)


def print_task(task, task_num):
    '''
    This function will print task in a user friendly output

    Args:
        task (dictionary) : dictionary of task details
        task_num (int) : task number
    '''
    # Wrap long descriptions
    wrap_desc = textwrap.fill(
        task['description'], width= 45, initial_indent= "\n\t ",
        subsequent_indent= "\t ")

    # Print task details
    print("="*50)
    print(f"TASK NUMBER {task_num}\n{'-'*15}")
    print(f"\t{'Task:':25} {task['title']}")
    print(f"\t{'Assigned to:':25} {task['username']}")
    print(f"\t{'Date assigned:':25} {task['date_assigned']}")
    print(f"\t{'Due date:':25} {task['due_date']:}")
    print(f"\t{'Completed:':25} {task['completed']:}")
    print(f"\t{'Description:':<25}{wrap_desc}")
    print(f"{'-'*50}\n")


def reg_user(current_user):
    '''
    This function will register new users(admin only)

    Args:
        current_user (str): Username of the current user
    '''
    if current_user != "admin":
        print(f"{Fore.RED}You need to be an admin to register users")
        return

    # Load existing users
    users = load_users()
    print_header("Register user", current_user)

    # Loop to validate input
    while True:
        new_user = input("Enter new username: ").strip()
        if not new_user:
            print(f"{Fore.RED}'User' field cannot be blank")
            continue

        if  new_user in users:
            print(f"{Fore.RED}'{new_user}' already exist, try another user")
            continue

        password = getpass.getpass(f"Enter password for {new_user}: [hidden]"
                                   ).strip()
        confirm_pass = getpass.getpass("Confirm password: [hidden]").strip()

        if password != confirm_pass:
            print(Fore.RED + "Sorry, Passwords do not match. Try again.")
            continue

        users[new_user] = password
        save_users(users)
        print(f"{Fore.GREEN}{new_user} registered successfully.\n")
        break


def add_task(current_user):
    '''
    This function will create a new task

    Args:
        current_user (str): Username of the current user
    '''
    users = load_users()
    print_header("Add Task", current_user)
    while True:
        username = input("Enter Username to assign task to: ").strip()
        if username not in users:
            print(f"{Fore.RED}User {username} does not exist, try again.")
            continue

        title = input("Task title: ").strip()
        description = input("Description: ").strip()
        while True:
            due_date = input("Due date(e.g. 01 Jan 2025): ").strip()
            try:
                datetime.strptime(due_date, "%d %b %Y")
                break
            except ValueError:
                print(Fore.RED + "Invalid date format, try(e.g. 01 Jan 2025)")

        current_date = date.today().strftime("%d %b %Y")
        tasks = load_tasks()
        tasks.append({
            'username' : username,
            'title' : title,
            'description' : description,
            'date_assigned' : current_date,
            'due_date' : due_date,
            'completed' : 'No'
        })
        save_tasks(tasks)
        print(Fore.GREEN + f"{title} assigned to {username} successfully.\n")
        return


def view_all():
    '''
    This function will view all tasks in tasks.txt
    '''
    tasks = load_tasks()
    if not tasks:
        print(f"{Fore.RED}No tasks available.\n")
        return

    for t, task in enumerate(tasks, 1):
        print_task(task, t)


def view_mine(current_user):
    '''
    This function will view current user's tasks

    Args:
        current_user (str): Username of the current user
    '''
    tasks = load_tasks()
    user_tasks = [task for task in tasks if task['username'] == current_user]
    print_header("Your tasks", current_user)

    if not user_tasks:
        print("No tasks available for you.\n")
        return

    # Loop to validate input
    while True:
        for i, task in enumerate(user_tasks, 1):
            print_task(task, i)

        choice = input("Enter task number to edit(-1 to return): ").strip()
        if choice == '-1':
            return
        try:
            choice = int(choice) - 1
        except ValueError:
            print(f"{Fore.RED}Invalid input. Enter a task number or '-1'")
            continue

        if choice < 0 or choice >= len(user_tasks):
            print(f"{Fore.RED}Input out of range.\n")
            continue

        task = user_tasks[choice]
        if task['completed'] == 'Yes':
            print(f"{Fore.RED}Task is marked completed, cannot edit.\n")
            continue

        option = input("Enter (m)-to mark completed, (e)-to edit task: "
                       ).strip().lower()
        if option == 'm':
            task['completed'] = 'Yes'
            save_tasks(tasks)
            print(f"{Fore.GREEN}Task marked as completed.\n")

        elif option == 'e':
            new_user = input("Enter username to assign task to(Enter to skip)"
            ": ").strip()

            if new_user and new_user not in load_users():
                print(f"{Fore.RED}Error: '{new_user}' does not exist.\n")
                continue

            new_due_date = input("Enter due date(eg. 01 Jan 2025)"
            "Enter to skip: ").strip()

            if new_due_date:
                try:
                    datetime.strptime(new_due_date, "%d %b %Y")
                    task['due_date'] = new_due_date
                except ValueError:
                    print(f"{Fore.RED}Invalid date format(e.g. 01 Jan 2025).")
                    continue

            if new_user:
                task['username'] = new_user
            if new_due_date:
                task['due_date'] = new_due_date
            save_tasks(tasks)
            print(f"{Fore.GREEN}Task updated successfully.")

        else:
            print(f"{Fore.RED}Error: Invalid option. Use (m) or (e)")


def view_completed():
    '''
    This function will display completed tasks
    '''
    tasks = load_tasks()
    completed_tasks = [task for task in tasks if task['completed'] == 'Yes']
    if not completed_tasks:
        print("No completed tasks.\n")
        return
    for i, task in enumerate(completed_tasks, 1):
        print_task(task, i)


def delete_task():
    '''
    This function will delete a task(admin only)
    '''
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.\n")
        return

    view_all()

    while True:
        try:
            task_num = int(input("Enter a task number to delete: "))
        except ValueError:
            print(f"{Fore.RED}Invalid input, enter a number\n")
            return

        if task_num < 1 or task_num > len(tasks):
            print(f"{Fore.RED}Task '{task_num}' does not exist.\n")
            return

        deleted = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"{Fore.GREEN}Task '{deleted['title']}' deleted successfully.\n")
        break


def overdue_task(tasks, today):
    '''
    This function will yield overdue tasks
    '''
    for t in tasks:
        if (
            t['completed'].lower() == 'no'
            and datetime.strptime(t['due_date'], '%d %b %Y').date() < today
            ):
            yield t


def pcnt(num1, num2):
    '''
    This function will help calculate the percentage(pcnt)
    and return the value
    '''
    return round((num1 / num2 * 100), 2) if num2 else 0


def write_report(username, tasks, total_tasks, f, today):
    '''
    This function will help write a report for a single user

    Args:
        username (str): username of the user
        tasks (list): list of task dictionaries
        total_tasks (int): total number of tasks
        f (file): file object to write report to
        today (date): current date
    '''
    user_tasks = [t for t in tasks if t['username'] == username]
    tasks_list = list(user_tasks)
    count = len(tasks_list)
    completed = len([t for t in user_tasks if t[
                    'completed'].lower() == 'yes'])
    uncomplete = count - completed
    overdue = sum(1 for t in overdue_task(tasks_list, today))

    f.write(f"  {'Username:':25} {username}\n")
    f.write(f"  {'Total tasks assigned:':25} {count}\n")
    f.write(f"  {'Total tasks %:':25} {pcnt(count, total_tasks):.2f}%\n")
    f.write(f"  {'Completed tasks %:':25} {pcnt(completed, count):.2f}%\n")
    f.write(f"  {'Uncompleted %:':25} {pcnt(uncomplete, count):.2f}%\n")
    f.write(f"  {'Overdue %:':25} {pcnt(overdue, count):.2f}%\n\n")


def generate_report():
    '''
    This function will generate reports
    '''
    tasks = load_tasks()
    users = load_users()
    today = date.today()

    total_tasks = len(tasks)
    completed = sum([1 for t in tasks if t['completed'].lower() == 'yes'])
    uncompleted = total_tasks - completed
    overdue = sum(1 for t in tasks
                  if t['completed'].lower() == 'no' and
                  datetime.strptime(t['due_date'], '%d %b %Y').date() < today)

    try:
        # Generate task overview file(f is file)
        with open("task_overview.txt", "w", encoding= "utf-8") as f:
            f.write("TASK OVERVIEW:\n")
            f.write(f"  {'Total tasks:':25} {total_tasks}\n")
            f.write(f"  {'Completed tasks:':25} {completed}\n")
            f.write(f"  {'Uncompleted tasks:':25} {uncompleted}\n")
            f.write(f"  {'Overdue tasks:':25} {overdue}\n")
            f.write(f"  {'Incomplete %:':25} {pcnt(uncompleted, total_tasks):.2f}%")
            f.write(f"\n  {'Overdue %:':25} {pcnt(overdue, total_tasks):.2f}%\n")
    except OSError as e:
        print(f"{Fore.RED}Error writing to file: {e}")

    try:
        # Generate user overview file(f is file)
        with open("user_overview.txt", "w", encoding= "utf-8") as f:
            f.write("USER OVERVIEW:\n")
            f.write(f"  {'Total users:':25} {len(users)}\n")
            f.write(f"  {'Total tasks:':25} {total_tasks}\n")
            f.write("\nSTATISTICS:\n")
            for username in users:
                write_report(username, tasks, total_tasks, f, today)

    except OSError as e:
        print(f"{Fore.RED}Error writing to file: {e}")

    print(f"{Fore.GREEN}Report generated successfully.\n")


def display_statistics():
    '''
    This function will display statistics from generate report
    '''
    if not (os.path.exists("task_overview.txt")
    and os.path.exists("user_overview.txt")):
        generate_report()
    try:
        with open("task_overview.txt", "r", encoding= "utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{Fore.RED}Error reading file: {e}")
    try:
        with open("user_overview.txt", "r", encoding= "utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{Fore.RED}Error reading file")


# ==== Login Section ====
def login():
    '''
    Allow a username to login.
    - Read usernames and passwords from the username.txt file
    - Use a dictionary to store a list of usernames and
      passwords from the file.
    - Use a while loop to validate your username name and password
    '''
    users = load_users()
    attempts = 3
    while attempts > 0:
        print_header("Login")
        username = input(" Username: ").strip()
        password = getpass.getpass(" Password: [hidden input]").strip()
        print("-"*50)

        if username in users and users[username] == password:
            print(f"{Fore.GREEN}Login successful.")
            return username

        attempts -= 1
        print(f"{Fore.RED}Wrong username/password combination.")
        print(f"{Fore.RED}Try again: {attempts} attempts left.")
        print("-"*40)

    print(f"{Fore.RED}Maximum attempts reached. Exiting.\n")
    exit()


def main_menu():
    '''
    Menu when user login successfully
    '''
    username = login()
    while True:
        if username == "admin":
            print_header("Admin Menu", username)
            menu = input(
        '''\nSelect one of the following options:
    r - register a username
    a - add task
    va - view all tasks
    vm - view my tasks
    vc - view completed tasks
    del - delete tasks
    ds - display statistics
    gr - generate reports
    e - exit
Enter option: 
'''
    ).lower()

        else:
           # Present the menu to the username and
            # make sure that the username input is converted to lower case
            print_header("Menu", username)
            menu = input(
            '''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
Enter option: 
'''
    ).lower()

        if menu == 'r':
            reg_user(username)

        elif menu == 'a':
            add_task(username)

        elif menu == 'va':
            print_header("All tasks", username)
            view_all()

        elif menu == 'vm':
            view_mine(username)

        elif menu == 'vc':
            print_header("Completed tasks", username)
            view_completed()

        elif menu == 'del':
            print_header("Delete task", username)
            delete_task()

        elif menu == 'gr':
            print_header("Generate report", username)
            generate_report()

        elif menu == 'ds':
            print_header("Statistics", username)
            display_statistics()

        elif menu == 'e':
            print_header("Logging out...", username)
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please try again")


# Main function, program starts
if __name__ == "__main__":
    main_menu()
