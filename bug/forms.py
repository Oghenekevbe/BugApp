from django import forms
from .models import Bug

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


class AddBugForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    bug_type = forms.CharField(max_length=225, widget=forms.TextInput(attrs={"class": "form-control"}))
    status = forms.ChoiceField(choices=STATUSES, required=False)

    class Meta:
        model = Bug
        fields = ("description", "bug_type", "status")
