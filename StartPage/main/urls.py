from django.urls import path
from . import views

# Create your views here.
app_name = 'main'

urlpatterns = [
	path('', views.index, name = 'index')
]