from django.db import models

import datetime


def process_input_date(input_date):
    """Parse the input date string and return a date object

    The object returned is of the type datetime.date.
    :param input_date: The date in the ISO format yyyy-mm-dd
    :return: A datetime.date object representing the input date
    :raise IndexError and ValueError
    """
    try:
        input_date_data = input_date.split("-")
        year = int(input_date_data[0])
        month = int(input_date_data[1])
        day = int(input_date_data[2])
        return datetime.date(year=year, month=month, day=day)
    except (IndexError, ValueError) as e:
        print("Invalid date format")
        raise


def calculate_date_diff_from_today(date_object):
    """Calculates the absolute difference between input date and today's date.

    :param date_object: The datetime.date object representing the input date
    :return: the absolute difference of the two dates as a datetime.timedelta object.
    """
    today = datetime.date.today()
    difference = abs(today - date_object)
    return date_object, today, difference
