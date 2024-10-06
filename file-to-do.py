import json  

tasks = []  
prior_and_due = {}  

# Function to load tasks from a file  
def load_tasks(filename="tasks.json"):  
    global tasks, prior_and_due  
    try:  
        with open(filename, "r") as file:  
            data = json.load(file)  
            tasks = data.get("tasks", [])  
            prior_and_due = data.get("prior_and_due", {})  
            print("Tasks loaded from file.")  
    except FileNotFoundError:  
        print("No saved tasks found. Starting fresh.")  
    except json.JSONDecodeError:  
        print("Error reading tasks from file. Starting fresh.")  

# Function to save tasks to a file  
def save_tasks(filename="tasks.json"):  
    data = {  
        "tasks": tasks,  
        "prior_and_due": prior_and_due  
    }  
    with open(filename, "w") as file:  
        json.dump(data, file)  
    print("Tasks saved to file.")  

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
        tasks.remove(task_name)  
        del prior_and_due[task_name]  
    else:  
        print(f"{task_name} not found.")  

def main():  
    load_tasks()  # Load existing tasks at the start  

    while True:  
        print("\nPress 1 to Add!")  
        print("Press 2 to Delete!")  
        print("Press 3 to Mark as Complete!")  
        print("Press 4 to View Tasks!")  
        print("Press 5 to Save Tasks!")  # Added option to save tasks  
        print("Press 6 to Exit!")  
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
                save_tasks()  # Save tasks before exiting  
            elif task == 6:  
                print("Exiting the program.")  
                save_tasks()  # Save tasks on exit  
                break  
            else:  
                print("Invalid option, please try again.")  
        except ValueError:  
            print("Please enter a valid number.")  

if __name__ == "__main__": 
    main() 
    