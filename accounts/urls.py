from django.urls.conf import path
from accounts.views import CreateProfile, ListProfile


urlpatterns = [
    path('show_profiles/',ListProfile.as_view()),
    path('create_profile/',CreateProfile.as_view()),
]
