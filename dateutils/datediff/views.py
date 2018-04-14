from django.shortcuts import render

from .models import process_input_date, calculate_date_diff_from_today
from .models import add_days_to_date as models_add_days_to_date


# Create your views here.
def difference_from_today(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        if from_date:
            print("From date : {}".format(from_date))
            try:
                from_date, today, difference = calculate_date_diff_from_today(process_input_date(from_date))
                output_text = "The difference between the date {} and today's date {} is {} days.".format(from_date,
                                                                                                          today,
                                                                                                          difference.days)
            except ValueError as e:
                print("Error while processing input date.", e)
                output_text = "Invalid date format {}. {}".format(from_date,
                                                                     "Date must be between 0001-01-01 and 9999-12-31")
            context = {"output": output_text}
            print(output_text)
        else:
            print("No date entered")
        return render(request, "datediff/date_diff.html", context=context)
    else:
        return render(request, "datediff/date_diff.html")


def add_days_to_date(request):
    if request.method == "POST":
        date = request.POST.get("from_date")
        days = int(request.POST.get("days"))
        operation = request.POST.get("operation")
        context = None
        if date and days:
            try:
                if operation == "-":
                    days = -days
                input_date = process_input_date(date)
                new_date = models_add_days_to_date(input_date, days)
                output_text = "{} {} {} days is {}".format(input_date, operation, abs(days), new_date)
            except ValueError as e:
                output_text = "Invalid date format {}. {}".format(date,
                                                                     "Date must be between 0001-01-01 and 9999-12-31")

            context = {"output": output_text}
        return render(request, "datediff/add_days.html", context=context)
    else:
        return render(request, "datediff/add_days.html")
