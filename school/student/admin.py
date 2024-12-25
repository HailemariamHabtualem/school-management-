from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'date_of_birth', 'gender', 'address', 'phone')
    search_fields = ('user__username', 'student_id')
    list_filter = ('gender', 'date_of_birth')

# Register your models here.
