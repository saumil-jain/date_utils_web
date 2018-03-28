from django.shortcuts import render

from .models import process_input_date, calculate_date_diff_from_today


# Create your views here.
def difference_from_today(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        if from_date:
            print("From date : {}".format(from_date))
            from_date, today, difference = calculate_date_diff_from_today(process_input_date(from_date))
            output_text = "The difference between the date {} and today's date {} is {} days.".format(from_date,
                                                                                                      today,
                                                                                                      difference.days)
            context = {"output": output_text}
            print(output_text)
        else:
            print("No date entered")
        return render(request, "datediff/date_diff.html", context=context)
    else:
        return render(request, "datediff/date_diff.html")
