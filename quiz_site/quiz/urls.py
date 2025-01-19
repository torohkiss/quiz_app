from django.urls import path
from . import views

urlpatterns = [
        path('question/<int:question_id>/', views.question_view, name='question'),
    ]
