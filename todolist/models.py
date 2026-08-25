from django.db import models

# This model stores a single todo task.
# Each task has a text field called 'task' and a boolean field called 'checked'.
class ToDoList(models.Model):
    task = models.CharField(max_length=255, null=False, blank=False)
    checked = models.BooleanField(default=False)
