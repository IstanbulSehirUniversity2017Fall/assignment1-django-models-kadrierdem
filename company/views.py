from django.shortcuts import render
from .models import DepartmentModel,PersonalModel
# Create your views here.

def personal_info(request,index):
    personal=PersonalModel.objects.get(pk=index)
    return render(request,'personal.html',{'personal':personal})

