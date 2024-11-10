tasks_and_due = {}

def main():

    def add_tasks():
        task_name = input("task_name: ")
        
        if task_name in tasks_and_due:
            print(f"{task_name} already exists")
        else:
            date = int(input("DUE_DATE: "))
            tasks_and_due[task_name] = date

            print(f"TASK:{task_name}, with DUE_DATE:{date} added successfully")
    

    def remove_tasks():
        task_name = input("TASK_NAME: ")
        if task_name not in tasks_and_due:
            print(f"{task_name} not found")
        else:
            del(tasks_and_due[task_name])
            print(f"TASK:{task_name} deleted successfully")
    def mark_as_complete():
        task_name = input("TASK_NAME: ")
        if task_name not in tasks_and_due:
            print(f"{task_name} not found")
        else:
            del(tasks_and_due[task_name])
            print(f"TASK: {task_name} marked as complete ")
    def view_all_tasks():
        if tasks_and_due:
            print("AVAILABLE TASKS")
            for task_name, date in tasks_and_due.items():
             tasks_and_due[task_name] = date
             print(f"{task_name}:{date}")

    while True:
        print("1.Add new task:\n2.Remove task:\n3.view_all_tasks: ")
        user = input("press the corresponding numbers for the service you need ")
        if user == "1":
            add_tasks()
        elif user == "2":
            remove_tasks()
        elif user == "3":
            view_all_tasks()
        elif user == "4":
            mark_as_complete()
        else:
            print("please enter 1,2 or 3 ")

if __name__ == "__main__":
    main()

