from django.contrib import admin
from project.models import MyModel
from project.models import student


admin.site.register(MyModel)
admin.site.register(student)