from django.urls import path
from . import views

urlpatterns = [
        path('', views.all, name='all_questions'),
        #path('question/<int:question_id>/', views.question_view, name='question'),
        path('submit/', views.submit_answers, name='submit_answers'),
    ]
