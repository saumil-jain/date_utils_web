from django.shortcuts import render


def home(request):
    return render(request, "dateutils/home.html")
