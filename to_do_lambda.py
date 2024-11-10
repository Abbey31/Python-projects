tasks_and_due = {}  # Dictionary to hold tasks and their due dates  

def main():  
    # Lambda functions for each operation  
    add_task = lambda task_name, due_date: tasks_and_due.update({task_name: due_date}) if task_name not in tasks_and_due else f"Task '{task_name}' already exists."  
    remove_task = lambda task_name: tasks_and_due.pop(task_name, f"Task '{task_name}' not found.")  # Use pop to remove the key and return a message if not found  
    mark_completed = lambda task_name: tasks_and_due.pop(task_name, f"Task '{task_name}' not found.")  # Same logic as remove  
    view_tasks = lambda: [print(f"Task: '{task}', Due Date: '{due}'") for task, due in tasks_and_due.items()] if tasks_and_due else print("No tasks available.")  

    while True:  
        print("\nOptions:")  
        print("1. Add new task")  
        print("2. Remove task")  
        print("3. Mark task as complete")  
        print("4. View all tasks")  
        print("5. Exit")  
        
        user_choice = input("Please enter the corresponding number for the service you need: ")  
        
        if user_choice == "1":  
            task_name = input("Enter task name: ")  
            due_date = int(input("Enter due date (in simple integer format e.g., '20230101'): "))  
            result = add_task(task_name, due_date)  
            if isinstance(result, str):  
                print(result)  # Print any messages returned  
            else:  
                print(f"Task '{task_name}' with due date '{due_date}' added successfully.")  
                
        elif user_choice == "2":  
            task_name = input("Enter task name to remove: ")  
            message = remove_task(task_name)  
            print(message)  
            
        elif user_choice == "3":  
            task_name = input("Enter task name you want to mark as complete: ")  
            message = mark_completed(task_name)  
            print(message)  
            
        elif user_choice == "4":  
            print("Current tasks:")  
            view_tasks()  # Call the lambda function to view tasks  
            
        elif user_choice == "5":  
            print("Exiting the program.")  
            break  
            
        else:  
            print("Invalid input. Please enter a number from 1 to 5.")  
