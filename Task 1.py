# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added:", task)

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

# Function to remove a task by its index
def remove_task():
    list_tasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print("Task removed:", removed_task)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Main loop to run the To-Do List application
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exit!")
        break
    else:
        print("Invalid choice. Please try again.")
