## Import Classes and Libraries
from classes.tasks import create_task, create_database
import random

# Example tasks that could be added to database
# clean_btrm = create_task("Clean bathroom","Clean shower, toilet & floor","8/10/2023","High")

# fix_light = create_task("Fix lightbulb","Replace lightbulb in living room","24/10/2023","High")

### Initiate Task Management Programme
running= True
task_database = create_database("task_database")

while running:
    try:
        print(f'\n############################################################################')
        print(f'########################## TASK MANAGEMENT SYSTEM ##########################')
        print(f'############################################################################\n')
        choice = input(f'Please select an option:\n1) Add Task\n2) Delete Task\n3) View Tasks\n4) Exit\n')
        index = int(choice) - 1
        if index == 0:
            new_task_title = input("Please enter the title of your task\n") 
            new_task_descr = input("Please enter a brief description of your task\n")
            new_task_due = input("Please enter the due date of this task\n")
            new_task_priority = input("Please enter the priority of this task\n")
            new_task = create_task(new_task_title,new_task_descr,new_task_due, new_task_priority)
            task_database.add_tasks([new_task])
            print(f'\n############################################################################')
            print(f'{new_task_title} was successfully added to the database.')
            print(f'############################################################################\n') 
        if index == 1:
            task_to_delete = input("Please enter the title of the task you want to remove\n")
            try:
                task_database.delete_task_by_title(task_to_delete)
                print(f'\n############################################################################')
                print(f'{task_to_delete} was successfully deleted.')
                print(f'############################################################################\n')
            except ValueError:
                print(f'\n############################################################################')
                print(f'Sorry "{task_to_delete}" isn\'t a valid choice. Please try again.')
                print(f'############################################################################\n')
        
        if index == 2:
            print(f'\n############################################################################')
            task_database.print_task_names(due_date=True, priority=True)
            print(f'############################################################################\n')
        
        if index == 3:
            running = False
        
    except ValueError:
        print(f'\n############################################################################')
        print("Sorry that is not a valid choice. Please try again.")
        print(f'############################################################################\n')