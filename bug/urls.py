from django.urls import path
from .views import *


urlpatterns = [
    path("bug_list/", BugListView.as_view(), name="bug_list"),
    path("bug_detail/<int:pk>/", BugDetailView.as_view(), name="bug_detail")
]