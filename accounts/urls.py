from django.urls.conf import path
from accounts.views import ListProfile


urlpatterns = [
    path('show_profiles',ListProfile.as_view()),
]
