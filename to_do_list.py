
tasks = []
prior_and_due = {}

print("Welcome to my to_do_app!")

    
def add_tasks():
    task_name = input("Enter the name of the task you want to add: ")
    if task_name in tasks:
        print(f"{task_name} already exists.")
    else:
        tasks.append(task_name)
        due_date = input("enter the due date:")
        prior_and_due[task_name] = due_date
        print(f" {task_name} added successfully ")  

def mark_task_as_complete():
     pass

def remove_task():
     task_name = input("type the name of the task you want to delete!: ")
     if task_name not in tasks:
         print(f"{task_name} not found")
     else:
         tasks.remove(task_name)
         del prior_and_due[task_name]
         print(f"{task_name} deleted successfully")
while True:
    task_name = input("\nPress 1 to add a new task:\n2 to delete a task:\n 3 to mark as complete: ")
    if task_name == '1':
        add_tasks()
    elif task_name == '2':
         remove_task()
else:
        print("Enter 1, 2 or 3")
