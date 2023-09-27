## Import Classes and Libraries
from classes.tasks import create_task, create_database
import random

# Create database to store tasks
task_database = create_database("task_database")

# Create tasks to add to database
clean_btrm = create_task("Clean bathroom","Clean shower, toilet & floor","8/10/2023","High")

fix_light = create_task("Fix lightbulb","Replace lightbulb in living room","24/10/2023","High")

# Add tasks to database
task_database.add_task([clean_btrm, fix_light])

# Print task names in database
task_database.print_task_names(due_date=True, priority=True)