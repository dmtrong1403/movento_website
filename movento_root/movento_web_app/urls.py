from django.urls import path
from . import views
from .sitemaps import SubCategorySitemap, DetailSubCategorySitemap, DetailPostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'SubCategorySitemap': SubCategorySitemap,
    'DetailSubCategorySitemap': DetailSubCategorySitemap,
    'DetailPostSitemap': DetailPostSitemap,
    'StaticViewSitemap': StaticViewSitemap,
}

urlpatterns = [
    path("", views.index, name="home"),
    path("thiet-ke-thi-cong/<str:subcatename>", views.subcategory, name="service_subcategory"),
    path("thiet-ke-thi-cong/<str:subcatename>/<str:detailsubcatename>", views.detailsubcategory, name="service_detailsubcategory"),
    path("thiet-ke-thi-cong/<str:subcatename>/<str:detailsubcatename>/<str:detailpostname>", views.detailpost, name="service_detailpost"),
    path("san-pham/<str:subcatename>", views.subcategory, name="product_subcategory"),
    path("san-pham/<str:subcatename>/<str:detailsubcatename>", views.detailsubcategory, name="product_detailsubcategory"),
    path("san-pham/<str:subcatename>/<str:detailsubcatename>/<str:detailpostname>", views.detailpost, name="product_detailpost"),
    path("lien-he", views.contact, name="contact"),
    path("yeu-cau-tu-van", views.submit_request, name="success"),
    path("ho-so-nang-luc", views.about, name="about"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="")
]