from django.contrib import admin
from django.urls import path
from authentication import views as auth

urlpatterns = [
    path('user-exists', auth.UserExistsView.as_view()),
    path('login', auth.LoginView.as_view()),
    path('create-account', auth.CreateAccountView.as_view()),
    path('submit-otp', auth.SubmitOtpView.as_view()),
    path('reset-password', auth.ResetPasswordView.as_view()),
    path('forgot-otp', auth.ForgotOtpView.as_view()),
    path('resend-otp', auth.ResendOtpView.as_view()),
    path('resend-v-otp', auth.ResendVOtpView.as_view()),
    path('new-password', auth.NewPasswordView.as_view()),
]