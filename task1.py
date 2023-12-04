 # To-Do List Application

tasks = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update task")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n===== To-Do List =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("Eter a new task: ")
    tasks.append(new_task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1

    if 0 <= task_index < len(tasks):
        updated_task = input("Enter the updated task: ")
        tasks[task_index] = updated_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def remove_task():
    view_task()
    task_index = int(input("Enter the task number to remove: ")) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
         remove_task()
    elif choice == '5':
        print("Exiting the To-Do List applicaton. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


