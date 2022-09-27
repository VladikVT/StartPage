from django.urls import path
from . import views

# Create your views here.
app_name = 'main'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('add_fav_site', views.addFavSite, name = 'addFavSite'),
	path('<int:siteID>/del_fav_site', views.delFavSite, name = 'delFavSite'),
	path('add_news_site', views.addNewsSite, name = 'addNewsSite'),
	path('<str:siteName>/del_news_site', views.delNewsSite, name = 'delNewsSite')
]