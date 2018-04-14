from django import forms

import datetime


class DateDiffFromTodayForm(forms.Form):
    from_date = forms.DateField(label="Enter date")


class AddDaysToDateForm(forms.Form):
    input_date = forms.DateField(label="Enter date")
    operation = forms.ChoiceField(choices=[("+", "Add (+)"), ("-", "Subtract (-)")])
    days = forms.IntegerField(min_value=1, max_value=3652058)
    # The max value is difference in days between
    # datetime.date.max and datetime.date.min

    def clean(self):
        """Override clean method for number of days validation

        This method validates the maximum number of days that can be added/subtracted
        from the input date, based on the difference between the input date and
        datetime.date.max/datetime.date.min
        """
        cleaned_data = super().clean()
        input_date = cleaned_data.get("input_date")
        operation = cleaned_data.get("operation")
        days = cleaned_data.get("days")
        if operation == "+" and days > (datetime.date.max - input_date).days:
            allowed_days = (datetime.date.max - input_date).days
            raise forms.ValidationError("For the input date {}, the number of days to add can't be greater than {}"
                                        .format(input_date, allowed_days))
        if operation == "-" and days > (input_date - datetime.date.min).days:
            allowed_days = (input_date - datetime.date.min).days
            raise forms.ValidationError("For the input date {}, the number of days to subtract can't be greater than {}"
                                        .format(input_date, allowed_days))
