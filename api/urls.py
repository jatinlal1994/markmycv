from django.contrib import admin
from django.urls import path

from api import views as api

urlpatterns = [
    path('get-profile', api.getProfile.as_view()),
    path('save-profile', api.saveProfile.as_view()),
    path('image/<slug:hashcode>', api.picture),
    path('upload-profile-pic', api.UploadProfilePic.as_view()),
    path('upload-image', api.UploadImage.as_view()),
    path('terms-of-use', api.termsOfUse),
    path('privacy-policy', api.privacyPolicy),
    path('download-primary-resume', api.DownloadPrimaryResume.as_view()),
]
