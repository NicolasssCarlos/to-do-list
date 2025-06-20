Simple Task Manager (Python + SQLite)
This is a basic Command-Line Task Manager built with Python and SQLite.
It allows users to add, view, complete, and delete tasks stored in a local database.

Features
Add new tasks

View all tasks

Mark tasks as complete

Delete tasks

All data is saved locally using SQLite

How it works
When you run the program, you'll see a menu like this:


1. To add a new task
2. To view your tasks
3. To update the status of your tasks
4. To delete a task
5. To quit the system
You just type the number for the option you want.

Tasks are shown like this:


1 - Go to the gym - To Do
2 - Play some games - Complete
You manage tasks by typing their ID number.

Requirements
Python 3.x

(No need to install any external libraries. Only uses Python's built-in sqlite3 module.)

How to run
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your-username/your-repo-name.git
Run the Python script:

nginx
Copiar
Editar
python your_script_name.py
Notes
All data is stored in a local file called tasks (SQLite database).

You can reset the data by deleting this file.
