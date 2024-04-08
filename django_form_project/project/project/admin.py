from django.contrib import admin
from project.models import MyModel
from project.models import Student


admin.site.register(MyModel)
admin.site.register(Student)