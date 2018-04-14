from django import forms


class DateDiffFromTodayForm(forms.Form):
    from_date = forms.DateField(label="Enter date")
