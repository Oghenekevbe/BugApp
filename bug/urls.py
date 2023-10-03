from django.urls import path
from .views import *


urlpatterns = [
    path("add_bug/", BugCreateView.as_view(), name="add_bug"),
    path("bug_list/", BugListView.as_view(), name="bug_list"),
    path("bug_detail/<int:pk>/", BugDetailView.as_view(), name="bug_detail")
]