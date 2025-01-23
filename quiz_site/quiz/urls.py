from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
        #path('', views.quiz_home, name='quiz_home'),
        path('', views.dashboard, name='dashboard'),
        path('quiz_home', views.quiz_home, name='quiz_home'),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('all/', views.all, name='all_questions'),
        path('reset-scores/', views.reset_scores, name='reset_scores'),
        path(
            'password-change/',
            auth_views.PasswordChangeView.as_view(),
            name='password_change'
        ),
        path(
            'password-change/done/',
            auth_views.PasswordChangeDoneView.as_view(),
            name='password_change_done'
        ),
    ]
