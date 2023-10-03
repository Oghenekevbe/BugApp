from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,ListView
from .forms import AddBugForm
from .models import Bug


# Create your views here.



class BugListView(ListView):
    model = Bug
    template_name = 'bug_list.html'
    context_object_name = 'bugs'


class BugDetailView(DetailView):
    model = Bug
    template_name = 'bug_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bug"] = self.get_object()
        return context
    


class BugCreateView(CreateView):
    model = Bug
    template_name = "add_bug.html"
    form_class = AddBugForm
    success_url = reverse_lazy('bug_list')

    

