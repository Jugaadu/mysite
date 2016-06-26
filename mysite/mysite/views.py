from django.shortcuts import render


def home(request):
    contest = {}
    template = "home.html"
    return render(request,template,context)
