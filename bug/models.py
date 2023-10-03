from django.db import models
from datetime import datetime

# Create your models here.


class Bug(models.Model):
    
    STATUSES =[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed'),
            ('reopened', 'Reopened'),
            ('duplicate', 'Duplicate'),
            ('invalid', 'Invalid'),
            ('wont_fix', "Won't Fix"),
    ]

    description = models.TextField()
    bug_type = models.CharField(max_length=225)
    report_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50, unique=True, choices=STATUSES)


    def __str__(self):
        return self.bug_type

