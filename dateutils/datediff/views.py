from django.shortcuts import render

from .models import process_input_date, calculate_date_diff_from_today
from .models import add_days_to_date as models_add_days_to_date
from .forms import DateDiffFromTodayForm, AddDaysToDateForm


# Create your views here.
def difference_from_today(request):
    output_text = None
    if request.method == "POST":
        form = DateDiffFromTodayForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data["from_date"]
            from_date, today, difference = calculate_date_diff_from_today(from_date)
            output_text = "The difference between the date {} and today's date {} is {} days.".format(from_date,
                                                                                                      today,
                                                                                                      difference.days)
    else:
        form = DateDiffFromTodayForm()

    return render(request, "datediff/date_diff.html", context={"form": form, "output": output_text})


def add_days_to_date(request):
    output_text = None
    if request.method == "POST":
        form = AddDaysToDateForm(data=request.POST)
        if form.is_valid():
            input_date = form.cleaned_data["input_date"]
            operation = form.cleaned_data["operation"]
            days = form.cleaned_data["days"]
            if operation == "-":
                days = -days
            new_date = models_add_days_to_date(input_date, days)
            output_text = "{} {} {} days is {}".format(input_date, operation, abs(days), new_date)
    else:
        form = AddDaysToDateForm()

    return render(request, "datediff/add_days.html", context={"form": form, "output": output_text})
