
from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = 'parents'

    def __str__(self):
        return self.user.username

class Learner(models.Model):
    name = models.CharField(max_length=50,default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    admission_number = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'learners'

    def __str__(self):
        # return self.user.username
          return f"{self.name} {self.grade} {self.admission_number}"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = 'assignments'

    def __str__(self):
        return f"{self.title} {self.description} {self.due_date} {self.uploaded_by}"

class Result(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    marks = models.IntegerField()
    remarks = models.TextField()

    class Meta:
        db_table = 'results'

    def __str__(self):
        return f"{self.learner.name} - {self.assignment.title} {self.marks} {self.remarks}"

class Feedback(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return f"Feedback by {self.parent.user.username}"
