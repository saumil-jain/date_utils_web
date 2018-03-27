from django.shortcuts import render


# Create your views here.
def difference_from_today(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        if from_date:
            print("From date : {}".format(from_date))
        else:
            print("No date entered")
        return render(request, "datediff/date_diff.html")
    else:
        return render(request, "datediff/date_diff.html")
