# Python To-Do List

A simple command-line based To-Do List application built using Python 3.12.4.

## Features

- Load tasks from a file (tasks.txt)
- Save tasks to a file
- View tasks
- Add new tasks
- Delete tasks

## Usage

1. Run the `todo_list.py` script.
2. The main menu will be displayed with the following options:
   - View Tasks
   - Add Task
   - Delete Tasks
   - Exit
3. Select an option by entering the corresponding number.
4. Follow the prompts for the selected option.
5. To exit the program, choose option 4 (Exit).

## Code Structure

The code is organized into the following functions:

- `load_tasks()`: Loads tasks from the `tasks.txt` file and appends them to the `tasks` list.
- `save_tasks()`: Saves the current tasks in the `tasks` list to the `tasks.txt` file.
- `view_tasks()`: Displays the current tasks in the `tasks` list.
- `add_task()`: Prompts the user to enter a new task and adds it to the `tasks` list.
- `delete_task()`: Displays the current tasks, prompts the user to enter a task number, and removes the corresponding task from the `tasks` list.

The main loop runs until the user chooses to exit (option 4). It continuously displays the menu and executes the selected function based on the user's input.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.

