from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("thiet-ke-thi-cong/<str:subcatename>", views.subcategory, name="service_subcategory"),
    path("thiet-ke-thi-cong/<str:subcatename>/<str:detailsubcatename>", views.detailsubcategory, name="service_detailsubcategory"),
    path("thiet-ke-thi-cong/<str:subcatename>/<str:detailsubcatename>/<str:detailpostname>", views.detailpost, name="service_detailpost"),
    path("san-pham/<str:subcatename>", views.subcategory, name="product_subcategory"),
    path("san-pham/<str:subcatename>/<str:detailsubcatename>", views.detailsubcategory, name="product_detailsubcategory"),
    path("san-pham/<str:subcatename>/<str:detailsubcatename>/<str:detailpostname>", views.detailpost, name="product_detailpost"),
]