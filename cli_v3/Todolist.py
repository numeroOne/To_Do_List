import json

def load_data(filename="todo.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(tasks, filename="todo.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def display_task(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n-- To-Do List --")
        for i, t in enumerate(tasks, start=1):
            status = "done" if t['done'] else "Not Done"
            print(f"{i}. {t['task']} [{status}]")

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_data(tasks)

def mark_task_done(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        print(f"Task {task_number} marked as done.")
    else:
        print("Invalid task number")

def main():
    tasks = load_data()
    while True:
        print("\n-- To-Do List CLI --")
        print("1. View Tasks")
        print("2. Mark Task as done")
        print("3. Add Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_task(tasks)
        elif choice == "2":
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_done(tasks, task_number)
            save_data(tasks)
        elif choice == "3":
            task = input("Enter Task: ")
            add_task(tasks, task)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
