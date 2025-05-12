📝 To-Do List Project V3.0 

# To-Do List CLI App (v3.0)

A simple Command-Line Interface (CLI) based To-Do List application built with Python.

## 📌 Features (v3.0)
- View all tasks with their completion status.
- Add new tasks.
- Save and load tasks from a JSON file.
- Structured with `main()` function and argument-based file handling.
- Gracefully handles missing or corrupted data files.

## 🚀 How to Use

1. Make sure Python 3 is installed on your system.
2. Run the application using:
   ```bash
   python todo_cli.py


📂 Project Structure
to_do_list/
└── cli/
    └── todo_cli.py   # Main CLI program (version 3.0)

📄 Example Output
-- To-Do List CLI --
1. View Tasks
2. Add Task
3. Exit
Choose an option: 1
No tasks yet.

💾 Data Persistence
Tasks are stored in todo.json using this structure:
[
    {
        "task": "Learn Python",
        "done": false
    }
]

🛠 Built With
- Python 3.x
- JSON for data storage
- Basic terminal input/output

📌 Versioning
This is version v3.0. Future improvements will be tracked with Git tags:
- v3.1: Mark tasks as done
- v3.2: Edit tasks
- v3.3: Search tasks
