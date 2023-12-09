from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'users/login.html')


#<link>rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"</link>