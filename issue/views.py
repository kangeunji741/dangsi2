from django.shortcuts import render, get_object_or_404
from .models import Issue


# Create your views here.
def issue(request):
    issues = Issue.objects.all()

    return render(request, 'issue/issue.html', {"issues": issues})


def issue_detail(request, id):
    issue = get_object_or_404(Issue, id=id)

    return render(request, 'issue/issue_detail.html', {"issue": issue})
