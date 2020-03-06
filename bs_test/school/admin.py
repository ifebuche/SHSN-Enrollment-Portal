from django.contrib import admin
from .models import Student, Counting, Course

class StudentAdmin(admin.ModelAdmin):
	list_display = ['fullname','student_no','course','score', 'grade', 'created_at', 'updated_at']

admin.site.register(Student, StudentAdmin)

# class CountingAdmin(admin.ModelAdmin):
# 	list_display = ['fullname','student_no','course','score', 'grade']

admin.site.register(Counting)

admin.site.register(Course)