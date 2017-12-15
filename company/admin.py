from django.contrib import admin
from .models import DepartmentModel,PersonalModel
# Register your models here.

admin.site.register(DepartmentModel)
admin.site.register(PersonalModel)