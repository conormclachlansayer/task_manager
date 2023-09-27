# Importing Libraries
import random

# Creating Classes

# Class is create task
class create_task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description        
        self.due_date = due_date
        self.priority = priority 
    
    def update_title(self, new_title):
        self.title = new_title
        return self.title

    def update_description(self, new_description):
        self.description = new_description
        return self.description
    
    def update_due_date(self, new_due_date):
        self.due_date = new_due_date
        return self.due_date
    
    def update_prioriy(self, new_priority):
        self.priority = new_priority
        return self.priority
    
class create_database:
    def __init__(self, database_name, tasks = []):
        self.database_name = database_name
        self.tasks = tasks

    def add_task(self, new_tasks):
        for task in new_tasks:
            self.tasks.append(task)
        return self.tasks
    
    def print_task_names(self, due_date = False, priority = False):
        i = 1
        print(f'Tasks to Complete:')
        for task in self.tasks:
            print(f'{i}) {task.title}') 
            if due_date: print(f'Due: {task.due_date}')
            if priority: print(f'Priority: {task.priority}')
            i += 1
    

    
