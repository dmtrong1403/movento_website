from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import SubCategorySitemap, DetailSubCategorySitemap, DetailPostSitemap, StaticViewSitemap

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
    path("san-pham/<str:cate_code>", views.product_category, name="product_category"),
    path("san-pham/<str:cate_code>/<str:product_code>", views.product_detail, name="product_detail"),
    path("tim-kiem-san-pham", views.search_product, name="search_product"),
    path("tim-kiem-san-pham/<str:tagname>", views.search_product_tagname, name="search_product_tagname"),
    path("lien-he", views.contact, name="contact"),
    path("yeu-cau-tu-van", views.submit_request, name="success"),
    path("ho-so-nang-luc", views.about, name="about"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="")
]