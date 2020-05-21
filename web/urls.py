from django.urls import path, re_path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='submit_income'),
    path('register/', view.register, name='register'),
]