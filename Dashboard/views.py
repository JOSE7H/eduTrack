from http.client import HTTPResponse

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Learner, Parent, Assignment, Result, Feedback

# @login_required
def dashboard(request):
    user = request.user


    # Learner Dashboard
    if hasattr(user, 'learner'):
        assignments = Assignment.objects.filter(is_published=True)
        results = Result.objects.filter(learner=user.learner)
        feedbacks = Feedback.objects.filter(learner=user.learner)
        return render(request, 'learner_dashboard.html', {
            'assignments': assignments,
            'results': results,
            'feedbacks': feedbacks,
        })

    # Parent Dashboard
    elif hasattr(user, 'parent'):
        learners = Learner.objects.filter(parent=user.parent)
        learner_results = {learner: Result.objects.filter(learner=learner) for learner in learners}
        feedbacks = Feedback.objects.filter(parent=user.parent)
        return render(request, 'parent_dashboard.html', {
            'learners': learners,
            'learner_results': learner_results,
            'feedbacks': feedbacks,
        })

    # Teacher Dashboard
    else:
        uploaded_assignments = Assignment.objects.filter(uploaded_by=user)
        return render(request, 'teacher_dashboard.html', {
            'uploaded_assignments': uploaded_assignments,
        })

def learner_dashboard(request):
    assignments = Assignment.objects.filter(learner=request.user)
    return render(request, 'learner_dashboard.html', {'assignments': assignments})


def parent_dashboard(request):
    learners = Learner.objects.filter(parent=request.user)
    assignments = Assignment.objects.filter(learners__in=learners)
    return render(request, 'parent_dashboard.html', {'learners': learners, 'assignments': assignments})

def teacher_dashboard(request):
    assignments = Assignment.objects.filter(teacher=request.user)
    learners = Learner.objects.filter(teacher=request.user)
    return render(request, 'teacher_dashboard.html', {'learners': learners, 'assignments': assignments})


