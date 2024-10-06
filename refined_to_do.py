tasks = []
prior_and_due = {}
def add_tasks():  
    task_name = input("Enter the name of the task you want to add: ")  
    if task_name in tasks:  
        print(f"{task_name} already exists.")  
    else:  
        tasks.append(task_name)  
        due_date = input("Enter due date for the task: ")  
        prior_and_due[task_name] = due_date  
        print(f"{task_name} added successfully with due date {due_date}.")  

def remove_task():  
    task_name = input("Type the name of the task you want to delete: ")  
    if task_name not in tasks:  
        print(f"{task_name} not found.")  
    else:  
        tasks.remove(task_name)  
        del prior_and_due[task_name]  
        print(f"{task_name} deleted successfully.")  

def mark_task_as_complete():  
    task_name = input("Type the name of the task you want to mark as complete: ")  
    if task_name in tasks:  
        print(f"{task_name} marked as complete.")  
        # Optionally remove or archive the task  
        tasks.remove(task_name)  
        del prior_and_due[task_name]  
    else:  
        print(f"{task_name} not found.")  

def main():  
    while True:  
        print("\nPress 1 to Add!")  
        print("Press 2 to Delete!")  
        print("Press 3 to Mark as Complete!")  
        print("Press 4 to View Tasks!")  
        print("Press 5 to Exit!")  
        try:  
            task = int(input("Select an option: "))  
            if task == 1:  
                add_tasks()  
            elif task == 2:  
                remove_task()  
            elif task == 3:  
                mark_task_as_complete()  
            elif task == 4:  
                print("Current tasks and due dates:")  
                for task, date in prior_and_due.items():  
                    print(f"{task} : {date}")  
            elif task == 5:  
                print("Exiting the program.")  
                break  
            else:  
                print("Invalid option, please try again.")  
        except ValueError:  
            print("Please enter a valid number.")  

if __name__ == "__main__":  
    main()  

