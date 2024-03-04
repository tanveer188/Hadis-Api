from django.urls import path,include
from .views import PostByDateView
urlpatterns = [
    path('<date>/', PostByDateView.as_view()),
]
