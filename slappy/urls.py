from django.urls import path
from slappy import views
app_name = 'slappy'


urlpatterns = [
    path('', views.home, name="home"),
    path("fetch/", views.fetch, name="fetch")
]
