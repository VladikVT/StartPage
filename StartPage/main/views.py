from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as req

# Create your views here.
def index(request):
	godot = getArticles(url="https://godotengine.org", nameClass='news-shortitem', nameTag='a', linkClass='news-shortitem', linkTag='a')
	dtf = getArticles(url="https://dtf.ru/gamedev/entries/new", nameClass='content-title content-title--short l-island-a', nameTag='div', linkClass='content-link', linkTag='a')

	return render(request, "index.html", {'articlesDTF': dtf, "articlesGodot": godot})

def getArticles(url, nameClass, nameTag, linkClass, linkTag):
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

	return articles