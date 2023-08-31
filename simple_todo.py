import json
print('Welcome to simple todo app.\n\n'.center(50))
tasks = []
users = dict()

main_menu = '''1. Display tasks
2. Add task
3. Remove task by index.
4. Quit'''


def add_task(task):
    if task not in tasks:
        tasks.append(task)
        print(f"Task '{task}' added\n")
    else:
        print('Tasks already have task.\n')


def remove_task(idx):
    if idx < len(tasks):
        task = tasks.pop(idx)
        print(f"Task '{task}' removed.\n")
    else:
        print('Invalid task or id\n')


def display_tasks():
    for idx, task in enumerate(tasks):
        print(f'{idx}: {task}')
    if len(tasks) == 0:
        print("You have no tasks")
    print()


def run(username):
    while True:
        print(main_menu)

        choice = input('>>> ')

        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input('Enter task: ')
            add_task(task)
        elif choice == '3':
            idx = input('Enter index of task: ')
            remove_task(idx)
        elif choice == '4':
            users[username] = tasks
            file = open("tasks.json", "w", encoding="utf-8")
            file.write(str(users))
            break
        else:
            print('invalid choice.')

def login():
    print("Welcome our log in page, pleasse fill in the following lines(Username, Password)")
    username = input("Pleasse input here your username: ")
    password = input("Pleasse input here your password: ")
    f = open("logins_passwords.json", "r", encoding="utf-8")
    file = json.load(f)
    t = open("tasks.json", "r", encoding="utf-8")
    task = json.load(t)
    if username in file.keys() and password in file.values():
        print("The login completed successfully")
        if username in task.keys():
            if len(task.values()) != 0:
                print("There are your tasks")
                print(task[username])
                run(username)
            else:
                print("You have not any tasks")
                print("Just add it")
                run(username)
                
    else:
        print("The username or password is invalid.")
        print("If you have no one account just create it.")
        create = input("If you have an account type 'y', if no type 'n': ")
        if create == "y":
            login()
        elif create == "n":
            registration()
    f.close()
    t.close()




def registration():
    print("Welcome our registration page, pleasse fill in the following lines(Username, Password):")
    username = input("Pleasse input here your username: ")
    password = input("Pleasse input here your password: ")
    users[username] = password
    log = False
    file = open("logins_passwords.json", "r", encoding="utf-8")
    f = json.load(file)
    if username not in f.keys():
        log = True
    else:
        print("Your Username is already exists (if it yours) just log in.")
        print()
        login()
    file.close()
    file = open("logins_passwords.json", "a", encoding="utf-8")
    if log:
        json.dump(users, file)
        print("The registration completed successfully: ")
        print("Now you can add or remove your tasks: ")
        print()
        run(username)
    file.close()


registration()


    
        



