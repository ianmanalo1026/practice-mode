from django.shortcuts import render
from django.db.models import F, Q
from .models import Student, Subject, Enrollment


def home(request):
    student = Student.objects.all()
    subject = Subject.objects.all()
    enrollment = Enrollment.objects.filter(student__name="Ian Manalo")
    context = {"student":student, "subject":subject, "enrollment":enrollment}
    
    return render(request, 'core/home.html', context)