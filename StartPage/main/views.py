from django.shortcuts import render

from .models import NewsSite, FavSite

from bs4 import BeautifulSoup
import requests as req

# Create your views here.
def index(request):
    favSites = FavSite.objects.order_by("id")
    
    articles = NewsSite.objects.order_by("id")
    completeArticles = []

    for i in articles:
        a = getArticles(siteName=i.siteName, url=i.url, nameClass=i.nameClass, nameTag=i.nameTag, linkClass=i.linkClass, linkTag=i.linkTag)
        completeArticles.append(a)

    return render(request, "index.html", {'articles': completeArticles, 'favSites': favSites})

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
