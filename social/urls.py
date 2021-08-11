from django.urls.conf import path
from social.views import ProfileAPIView

urlpatterns = [
    path('profile/',ProfileAPIView.as_view()),
]