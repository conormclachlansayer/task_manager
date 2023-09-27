## Import Classes and Libraries
from classes.tasks import create_task
import random


fix_light = create_task("Fix lightbulb","Replace lightbulb in living room","24/10/2023","High Priority")
print(fix_light.due_date)
fix_light.update_due_date("10/10/2023")

print(fix_light.due_date)