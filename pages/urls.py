from django.urls import path
from .views import HomePageView
from pages.apps import PagesConfig
app_name = PagesConfig.name
urlpatterns = [
 path('', HomePageView.as_view(), name='home'),
]

