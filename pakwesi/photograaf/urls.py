from django.conf.urls import url
from photograaf import views



urlpatterns = [
    url('',views.home, name='home'),
]
