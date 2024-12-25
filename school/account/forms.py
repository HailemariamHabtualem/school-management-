from django import forms
from student.models import Student
from teacher.models import Teacher

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'