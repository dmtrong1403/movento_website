from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import SubCategory, DetailSubCategory, DetailPost


class SubCategorySitemap(Sitemap):

    def items(self):
        return SubCategory.objects.all()


class DetailSubCategorySitemap(Sitemap):

    def items(self):
        return DetailSubCategory.objects.all()


class DetailPostSitemap(Sitemap):

    def items(self):
        return DetailPost.objects.all()


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about', 'contact']

    def location(self, item):
        return reverse(item)
