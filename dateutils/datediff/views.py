from django.shortcuts import render


# Create your views here.
def difference_from_today(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "datediff/date_diff.html")
