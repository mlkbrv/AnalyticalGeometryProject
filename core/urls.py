from django.urls import path
from . import views

urlpatterns = [
    # The main quiz page
    path('', views.quiz_view, name='quiz_page'),
    # Page after successful submission
    path('success/', views.success_view, name='success_page'),
]