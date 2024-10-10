names = []  
ages = []  
subjects = []  
scores = []  

def prompt_student_data():  
    while True:  
        name = input("\nKindly enter the student's name (or type 'done' to finish): ")  
        if name.lower() == 'done':  
         break  
         age = int(input("Enter the student's age: "))  
         subject = input("Enter the subject: ")  
         score = float(input("Enter the student's score: "))  
  
         names.append(name)  
         ages.append(age)  
         subjects.append(subject)  
         scores.append(score)  

def print_student_table():  
     print("\n| {:<15} | {:<5} | {:<20} | {:<5} |".format("Name", "Age", "Subject", "Score"))  
     print("-" * 60)  
     for i in range(len(names)):  
         print("| {:<15} | {:<5} | {:<20} | {:<5} |".format(names[i], ages[i], subjects[i], scores[i]))  
         
     if scores:  
         class_average = sum(scores) / len(scores)  
         print("\nClass Average Score: {:.2f}".format(class_average))  

prompt_student_data()
print_student_table()
        
