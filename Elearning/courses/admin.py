from django.contrib import admin
from .models import Courses, Student
# Register your models here.
# admin.site.register(Courses)
# admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
  list_display = ("name", "code", "gender",)
class CoursesAdmin(admin.ModelAdmin):
  list_display = ("name", "start_date", "end_date",'active') 
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Student, StudentAdmin)