TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            file.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def add_task(tasks):
    t = input("Enter a new task: ")
    tasks.append(t)
    print("Task added.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        ind = int(input("Enter task number to remove: ")) - 1
        if 0 <= ind < len(tasks):
            removed = tasks.pop(ind)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        c = input("Choose an option (1-4): ")

        if c == '1':
            show_tasks(tasks)
        elif c == '2':
            add_task(tasks)
        elif c == '3':
            remove_task(tasks)
        elif c == '4':
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
