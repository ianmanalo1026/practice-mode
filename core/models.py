from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    enroll = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    GRADE_STATUS = (
        ("A","A"),
        ("B", "B"),
        ("C", "C"),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    prelim_score = models.IntegerField(null=True, blank=True)
    midterm_score = models.IntegerField(null=True, blank=True)
    final_score = models.IntegerField(null=True, blank=True)
    sem_score = models.IntegerField(null=True, blank=True)
    sem_status = models.CharField(choices=GRADE_STATUS , max_length=50, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.student} enrolled in {self.subject}"