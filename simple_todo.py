import json

todos = []
users = []
current_user = None

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

def register_user(username, password):
    for user in users:
        if user['username'] == username:
            return None
    new_user = {'username': username, 'password': password, 'tasks': []}
    users.append(new_user)
    save_data("users.json", users)
    return new_user

def login_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def add_task(task, user):
    user['tasks'].append(task)
    save_data("users.json", users)

def remove_task(index, user):
    if 0 <= index < len(user['tasks']):
        user['tasks'].pop(index)
        save_data("users.json", users)

def mark_complete(index, user):
    if 0 <= index < len(user['tasks']):
        task = user['tasks'][index]
        user['tasks'][index] = (task[0], True)
        save_data("users.json", users)

def list_tasks(user):
    for i, (task, is_complete) in enumerate(user['tasks']):
        status = "Done" if is_complete else "Pending"
        print(f"{i}. {task} - {status}")

def main():
    global users, current_user
    users = load_data("users.json")

    while True:
        print("\nTo-Do App")
        if not current_user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = register_user(username, password)
                if user:
                    print("Registration successful!")
                    current_user = user
                else:
                    print("Username already exists.")
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = login_user(username, password)
                if user:
                    print("Login successful!")
                    current_user = user
                else:
                    print("Invalid credentials.")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"Logged in as {current_user['username']}")
            print("1. Add task")
            print("2. Remove task")
            print("3. Mark task as complete")
            print("4. List tasks")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter task: ")
                add_task((task, False), current_user)
            elif choice == "2":
                list_tasks(current_user)
                index = int(input("Enter index of task to remove: "))
                remove_task(index, current_user)
            elif choice == "3":
                list_tasks(current_user)
                index = int(input("Enter index of task to mark as complete: "))
                mark_complete(index, current_user)
            elif choice == "4":
                list_tasks(current_user)
            elif choice == "5":
                current_user = None
                print("Logged out successfully!")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()