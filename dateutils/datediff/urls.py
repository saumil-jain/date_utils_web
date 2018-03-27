from django.urls import re_path

from .views import difference_from_today


urlpatterns = [
    re_path(r"^days_till_today$", difference_from_today, name="datediff_days_till_today")
]
