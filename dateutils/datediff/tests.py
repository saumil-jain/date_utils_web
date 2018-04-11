from django.test import TestCase
from .models import add_days_to_date

import datetime


# Create your tests here.
class DateDiffTests(TestCase):

    def test_add_days_to_date(self):
        """Test addition of days to date"""
        date = datetime.date(year=2018, month=2, day=10)
        days = 5
        expected_date = datetime.date(year=2018, month=2, day=15)
        computed_date = add_days_to_date(date_object=date, days=days)
        self.assertEqual(computed_date, expected_date)

    def test_add_days_to_date_negative(self):
        """Test subtraction of days from date"""
        date = datetime.date(year=2018, month=2, day=10)
        days = -5
        expected_date = datetime.date(year=2018, month=2, day=5)
        computed_date = add_days_to_date(date_object=date, days=days)
        self.assertEqual(computed_date, expected_date)

    def test_add_days_to_date_overflow(self):
        """Test addition of very large number of days to date"""
        date = datetime.date(year=2018, month=2, day=10)
        days = -999999999
        with self.assertRaises(OverflowError):
            add_days_to_date(date_object=date, days=days)
