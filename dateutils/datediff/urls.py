from django.urls import re_path

from .views import difference_from_today


urlpatterns = [
    re_path(r"^difference_from_today$", difference_from_today, name="datediff_difference_from_today")
]
