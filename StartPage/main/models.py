from django.db import models

class NewsSite(models.Model):
	siteName = models.CharField("Site Name", max_length=50)
	url = models.TextField("Site URL")
	nameClass = models.CharField("Name Class", max_length=50)
	nameTag = models.CharField("Name Tag", max_length=50)
	linkClass = models.CharField("Link Class", max_length=50)
	linkTag = models.CharField("Link Tag", max_length=50)
	priority = models.IntegerField("Site Priority", default=0, blank=True)

class FavSite(models.Model):
	siteName = models.CharField("Site Name", max_length=50)
	url = models.TextField("Site URL")
	img = models.TextField("Site Img", blank=True)
	priority = models.IntegerField("Site Priority", default=0, blank=True)

class Settings(models.Model):
	bgURL = models.TextField("BackGround URL", blank=True)