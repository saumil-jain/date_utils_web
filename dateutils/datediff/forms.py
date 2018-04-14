from django import forms


class DateDiffFromTodayForm(forms.Form):
    from_date = forms.DateField(label="Enter date")


class AddDaysToDateForm(forms.Form):
    input_date = forms.DateField(label="Enter date")
    operation = forms.ChoiceField(choices=[("+", "Add (+)"), ("-", "Subtract (-)")])
    days = forms.IntegerField(min_value=1, max_value=3652058)
    # The max value is difference in days between
    # datetime.date.max and datetime.date.min
