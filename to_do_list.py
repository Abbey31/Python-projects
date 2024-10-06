
tasks = []
prior_and_due = {}
newtask = []
print("Welcome to my to_do_app!")
task = int(input("\npress1 to Add!:\npress2 to delete:\npress3 to mark_as_read: "))
    
def add_tasks():
    task_naame = input("Enter the name of the task you want to add: ")
    if task_naame  in tasks:
        print(f"{task_naame}already exist")
    else:
        tasks.append(task_naame)
        print(f"{task_naame} added succesfully")   
def remove_task():
    task_name = input("type the name of the task you want to delete!: ")
    if task_name not in tasks:
        print(f"{task_name} not found")
    else:
        del(task_name)
        print(f"{task_name} deleted successfully")
    
    

def mark_task_as_complete():
    priority_prompt = input("set task and due date?")
    for task,date in prior_and_due.items():
        print(f"{task}:{date}")

while True:
    if task == 1:
        add_tasks()
    elif task == 2:
        remove_task()
    elif task == 3:
        mark_task_as_complete()

if __name__ == "__main":
    main()

  


