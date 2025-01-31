from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
        #path('', views.quiz_home, name='quiz_home'),
        path('', views.dashboard, name='dashboard'),
        path('quiz_home', views.quiz_home, name='quiz_home'),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('all/', views.all, name='all_questions'),
        path('reset-scores/', views.reset_scores, name='reset_scores'),
        # path(
        #     'password-change/',
        #     auth_views.PasswordChangeView.as_view(),
        #     name='password_change'
        # ),
        # path(
        #     'password-change/done/',
        #     auth_views.PasswordChangeDoneView.as_view(),
        #     name='password_change_done'
        # ),
        # path(
        #     'password-reset/',
        #     auth_views.PasswordResetView.as_view(),
        #     name='password_reset'
        # ),
        # path(
        #     'password-reset/done/',
        #     auth_views.PasswordResetDoneView.as_view(),
        #     name='password_reset_done'
        # ),
        # path(
        #     'password-reset/<uidb64>/<token>/',
        #     auth_views.PasswordResetConfirmView.as_view(),
        #     name='password_reset_confirm'
        # ),
        # path(
        #     'password-reset/complete/',
        #     auth_views.PasswordResetCompleteView.as_view(),
        #     name='password_reset_complete'
        # ),
        path('register/', views.register, name='register'),
        path('', include('django.contrib.auth.urls')),
    ]
