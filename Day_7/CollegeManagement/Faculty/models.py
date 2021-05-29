from django.db import models

# Create your models here.
class Faculty(models.Model):
    # Note: No spaces are allowed in charfield function parameters and the function names are in CamelCase CharField. Observe it
    branches = (
        ('ECE','ece'),
        ('CSE','cse'),
        ('EEE','eee')
    )
    Name        = models.CharField(max_length=20,unique=True) 
    Age         = models.IntegerField(null=True)
    Branch      = models.CharField(max_length=10,choices=branches)
    Mobile      = models.CharField(max_length=10)
    Email       = models.EmailField(blank=True)

    def __str__(self):
        return self.Name + " " + self.Branch
