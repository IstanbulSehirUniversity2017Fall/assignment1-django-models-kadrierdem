from django.db import models

# Create your models here.


class DepartmentModel(models.Model):
    name=models.CharField(max_length=50)
    interest=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    budget=models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)+' '+self.name


class PersonalModel(models.Model):
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    salary=models.CharField(max_length=5)
    start_day=models.DateField()
    end_day=models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.id)+' '+self.first_name+' '+self.last_name