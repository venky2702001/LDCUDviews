from django.shortcuts import render
from view.models import *
from django.views.generic import ListView,DetailView
# Create your views here.

class SchoolList(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'