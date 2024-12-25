from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentRegistrationForm, TeacherRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        role = request.POST.get('role')
        if user_form.is_valid():
            user = user_form.save()
            if role == 'student':
                student_form = StudentRegistrationForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            elif role == 'teacher':
                teacher_form = TeacherRegistrationForm(request.POST)
                if teacher_form.is_valid():
                    teacher = teacher_form.save(commit=False)
                    teacher.user = user
                    teacher.save()
            messages.success(request, 'Account created successfully.')
            return redirect('accounts:login')
    else:
        user_form = UserCreationForm()
        student_form = StudentRegistrationForm()
        teacher_form = TeacherRegistrationForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'student_form': student_form,
        'teacher_form': teacher_form
    })