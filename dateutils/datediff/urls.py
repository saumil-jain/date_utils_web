from django.urls import re_path

from .views import difference_from_today, add_days_to_date


urlpatterns = [
    re_path(r"^difference_from_today$", difference_from_today, name="datediff_difference_from_today"),
    re_path(r"^add_days$", add_days_to_date, name="datediff_add_days")
]
