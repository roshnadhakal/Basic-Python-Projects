# Initialize an empty list to store tasks
tasks = []

# function to load tasks from a file

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                """adds each line from file to list,after removing any leading whitespace"""
                tasks.append(line.strip())
    except FileNotFoundError:
        print("No tasks file found")

#Save Tasks

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n") # string concatenation.

# View Tasks

def view_tasks():
    print("TO-Do-List:")
    for i , task in enumerate(tasks, start = 1):
        print(f"{i}.{task}") # formated string

# Add Tasks

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()

# Delete Tasks

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number you want to delete: "))
    try:
        del tasks[task_number - 1] #list indices start from 0.
        save_tasks()
    except IndexError:
         print("Invalid task number")


# Main Loop
load_tasks()
while True:
    print("\nTO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Tasks")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

        
