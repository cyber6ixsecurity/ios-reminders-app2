# To-Do List with File Saving

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return file.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except:
        print("Invalid selection.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()