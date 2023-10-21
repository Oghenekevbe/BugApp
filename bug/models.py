from django.db import models
from datetime import datetime

# Create your models here.


class Bug(models.Model):
    
    STATUSES =[
            ('new', 'New'),
            ('open', 'Open'),
            ('critical', 'Critical'),
            ('to_do', 'To Do'),
            ('assigned', 'Assigned'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed'),
            ('reopened', 'Reopened'),
            ('duplicate', 'Duplicate'),
            ('invalid', 'Invalid'),
            ('wont_fix', "Won't Fix"),
    ]
    BUG_TYPES = [
    ('functional', 'Functional Issue'),
    ('performance', 'Performance Issue'),
    ('security', 'Security Issue'),
    ('usability', 'Usability Issue'),
    ('compatibility', 'Compatibility Issue'),
    ('visual', 'Visual/Design Issue'),
    ('other', 'Other Issue'),
    ('database', 'Database Issue'),
    ('network', 'Network Issue'),
    ('crash', 'Application Crash'),
    ('installation', 'Installation Issue'),
    ('documentation', 'Documentation Issue'),
    ('data_loss', 'Data Loss Issue'),
    ('accessibility', 'Accessibility Issue'),
    ('authentication', 'Authentication Issue'),
    ('workflow', 'Workflow Issue'),
]


    description = models.TextField()
    bug_type = models.CharField(max_length=225, choices=BUG_TYPES)
    report_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50, choices=STATUSES)


    def __str__(self):
        return self.bug_type

