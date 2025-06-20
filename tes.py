import sqlite3

connection = sqlite3.connect("tasks")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    status TEXT
)
""")


print("Welcome to MyTaskList!")



def add_task():
    
    print("Let's create some tasks now")
    while True:
        tasks = input("Type some new task here: ")
        if tasks:
            cursor.execute("INSERT OR REPLACE INTO tasks (description, status) VALUES (?, ?)", (tasks, "To Do"))
            connection.commit()
            print("Your new task has been added to our database.")
            continuos_tasks = input('Would you like to add another task? Type "/yes/" or "/no/": ').lower()
            if continuos_tasks != "yes":
                print("Okay, I hope to see you later!")
                break
        else:
            print("Please type something valuable.")

def view_tasks():
    print("Okay, let's visualize all of your tasks here.")
    cursor.execute("SELECT * FROM tasks")
    tasks_to_see = cursor.fetchall()
    if tasks_to_see:
        for task in tasks_to_see:
            print(f"{task[0]} - {task[1]} - {task[2]}")
        print("That's all of your tasks in our database.")
    else:
        print("You don't have any tasks here yet. Add some to see them here.")

def complete_tasks():
    print("Have you completed any tasks?")
    print("Let's mark them as complete.")
    print("First of all, tell me which task you have done.")
    while True:
        cursor.execute("SELECT * FROM tasks")
        tasks_done = cursor.fetchall()
        if tasks_done:
            print("These are your tasks in our database:")
            for task in tasks_done:
                print(f"{task[0]} - {task[1]} - {task[2]}")
            tasks = input("Which task do you want to mark as complete?: ")
            if tasks.isdigit():
                tasks_int = int(tasks)
                cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", ("Complete", tasks_int))
                connection.commit()
                print("Your task is now marked as complete in our database.")
                continuos_tasks = input('Would you like to update other tasks? Type "/yes/" or "/no/": ').lower()
                if continuos_tasks != "yes":
                    print("That's it! Now, complete other tasks and come back here to get them marked.")
                    break
            else:
                print(f"We couldn't find the task '{tasks}' in our database. Please check if you typed it correctly.")
        else:
            print("You don't have any tasks in our database. Try to add some to see and update them here.")
            break

def delete_tasks():
    print("Let's delete some old tasks")
    while True:
        cursor.execute("SELECT * FROM tasks")
        tasks_to_delete = cursor.fetchall()
        if tasks_to_delete:
            print("These are your tasks in our database:")
            for task in tasks_to_delete:
                print(f"{task[0]} - {task[1]} - {task[2]}")
            deleted_tasks = input("Tell us which task you want to delete: ")
            if deleted_tasks.isdigit():
                deleted_tasks_int = int(deleted_tasks)
                cursor.execute("DELETE from tasks WHERE id = ?", (deleted_tasks_int,))
                connection.commit()
                print(f"The task '{deleted_tasks}' has been deleted.")
                continuos_task = input('Would you like to delete another task? Type "/yes/" or "/no/": ').lower()
                if continuos_task != "yes":
                    print("Okay, I hope to see you soon!")
                    break
            else:
                print("Please tell us which task you want to delete.")
        else:
            print("We can't find any of your tasks in our database. Please try again later.")
            break

while True:
    operations = [
        "1. To add a new task",
        "2. To view your tasks",
        "3. To update the status of your tasks",
        "4. To delete a task",
        "5. To quit the system"
    ]
    for ops in operations:
        print(ops)
    ops_option = input("Choose your operation: ")
    if ops_option == "1":
        add_task()
    elif ops_option == "2":
        view_tasks()
    elif ops_option == "3":
        complete_tasks()
    elif ops_option == "4":
        delete_tasks()
    elif ops_option == "5":
        print("Thank you for using this little application!")
        connection.close()
        break
    else:
        print("Please type one of the options.")