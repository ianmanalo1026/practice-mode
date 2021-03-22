from django.shortcuts import render
from django.db.models import F, Q, Count, Sum, ExpressionWrapper, IntegerField
from .models import Student, Subject, Enrollment


def home(request):
    student = Student.objects.all()
    subject = Subject.objects.all()
    sem_score = Enrollment.objects.all().update(
        sem_score=ExpressionWrapper(
            (F("prelim_score") + F("midterm_score") + F("final_score"))/3,
            output_field=IntegerField()))
    enrollment = Enrollment.objects.all()
    num_student = Enrollment.objects.all().count()
    context = {"student":student,
               "subject":subject,
               "enrollment":enrollment,
               "num_student":num_student
               }
    return render(request, 'core/home.html', context)