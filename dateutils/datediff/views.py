from django.shortcuts import render

from .models import process_input_date, calculate_date_diff_from_today, difference_between_two_dates
from .models import add_days_to_date as models_add_days_to_date
from .forms import DateDiffFromTodayForm, AddDaysToDateForm, DifferenceBetweenTwoDatesForm


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


def diff_dates(request):
    output_text = None
    if request.method == "POST":
        form = DifferenceBetweenTwoDatesForm(data=request.POST)
        if form.is_valid():
            date_1 = form.cleaned_data.get("date_1")
            date_2 = form.cleaned_data.get("date_2")
            days = difference_between_two_dates(date_1, date_2)
            output_text = "The difference between {} and {} is {} days.".format(date_1, date_2, days)
    else:
        form = DifferenceBetweenTwoDatesForm()

    return render(request, "datediff/diff_dates.html", context={"form": form, "output": output_text})
