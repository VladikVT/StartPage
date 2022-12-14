from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import NewsSite, FavSite, Settings

from bs4 import BeautifulSoup
import requests as req

# Create your views here.
def index(request):
	settings = Settings.objects.get(id = 1)

	favSites = FavSite.objects.order_by("-priority")
	
	articles = NewsSite.objects.order_by("-priority")
	completeArticles = []

	for i in articles:
		a = getArticles(siteName=i.siteName, url=i.url, 
						nameClass=i.nameClass, 
						nameTag=i.nameTag, 
						linkClass=i.linkClass, 
						linkTag=i.linkTag)
		completeArticles.append(a)

	return render(request, "index.html", {'articles': completeArticles, 'favSites': favSites, 'settings': settings})

def addFavSite(request):
	fs = FavSite.objects.order_by("id")
	fs.create(siteName = request.POST.get("siteName", False), 
				url = request.POST.get("url", False), 
				img = request.POST.get("img", False), 
				priority = request.POST.get("priority", 0))
	return HttpResponseRedirect(reverse("main:index"))

def delFavSite(request, siteID):
	FavSite.objects.get(id = siteID).delete()
	return HttpResponseRedirect(reverse("main:index"))

def addNewsSite(request):
	ns = NewsSite.objects.order_by("id")
	ns.create(siteName = request.POST.get("siteName", False), 
				url = request.POST.get("url", False), 
				nameClass = request.POST.get("nameClass", False), 
				nameTag = request.POST.get("nameTag", False), 
				linkClass = request.POST.get("linkClass", False), 
				linkTag = request.POST.get("linkTag", False), 
				priority = request.POST.get("priority", 0))
	return HttpResponseRedirect(reverse("main:index"))

def delNewsSite(request, siteName):
	NewsSite.objects.get(siteName = siteName).delete()
	return HttpResponseRedirect(reverse("main:index"))

def updateSettings(request):
	settings = Settings.objects.get(id = 1)

	settings.bgURL = request.POST.get("bgURL", False)

	settings.save()

	return HttpResponseRedirect(reverse("main:index"))

def getArticles(siteName, url, nameClass, nameTag, linkClass, linkTag):
	resp = req.get(url)
	soup = BeautifulSoup(resp.text, 'lxml')

	articles = []

	articleLinks = []
	articleNames = []

	for i in soup.find_all(linkTag, class_=linkClass, href=True):
		articleLinks.append(i['href'])
	
	for i in soup.find_all(nameTag, class_=nameClass):
		articleNames.append(i.text)

	articles.append(articleLinks)
	articles.append(articleNames)
	articles.append(siteName)

	return articles
