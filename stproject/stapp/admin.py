from django.contrib import admin
from django.contrib.admin import ModelAdmin

from stapp.models import Department, Course


# Register your models here.
class DeptAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DeptAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','fees','created','updated','no_of_seats','available']
    list_editable=['fees','no_of_seats','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Course,CourseAdmin)
