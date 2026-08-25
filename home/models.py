from django.db import models

# This model stores baby names in the database.
# Each record will have a single text field called 'name'.
class baby_names(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

