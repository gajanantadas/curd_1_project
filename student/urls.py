from django.urls import path
from . import views
urlpatterns = [
    path('stud/',views.student_api)
]
