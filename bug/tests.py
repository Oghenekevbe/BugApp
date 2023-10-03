from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Bug
from .views import BugCreateView, BugDetailView,BugListView

# Create your tests here.



class BugTestCase(TestCase):

    def setUp(self):
        Bug.objects.create(
            description='When clicking the submit button, the application crashes with an internal server error.',bug_type='Application Crash', 
            status='new',
            report_date = timezone.now()
            
            )
        
    def test_bug_type(self):
        bug= Bug.objects.get(description='When clicking the submit button, the application crashes with an internal server error.')
        self.assertEqual(bug.bug_type, 'Application Crash')

    def test_bug_status(self):
        bug= Bug.objects.get(bug_type='Application Crash')
        self.assertEqual(bug.status, 'new')

    def test_bug_description(self):
        bug = Bug.objects.get(status='new')
        self.assertEqual(bug.description,'When clicking the submit button, the application crashes with an internal server error.')

    def test_bug_report_date(self):
        bug = Bug.objects.get(status='new')
        current_time = timezone.now()

        #almost equal because of discrepancies
        self.assertAlmostEqual(bug.report_date, current_time, delta=timezone.timedelta(seconds=1))


class ViewTestCase(TestCase):

    def setUp(self):
        # Create a Bug object for testing
        self.bug = Bug.objects.create(
            description='When clicking the submit button, the application crashes with an internal server error.',
            bug_type='Application Crash',
            status='new',
            report_date=timezone.now()
        )

    
    def test_bug_detail_view(self):
        url = reverse('bug_detail',kwargs={'pk':self.bug.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_bug_detail_template(self):
        url = reverse('bug_detail',kwargs={'pk':self.bug.pk})
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'bug_detail.html')

    def test_list_bugs_view(self):
        url = reverse('bug_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_create_bug_view(self):
        url = reverse('add_bug')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

 


