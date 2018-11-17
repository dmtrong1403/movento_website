from django.core.paginator import Paginator
from django.shortcuts import render

from .models import SubCategory, DetailSubCategory, Content, CustomerComment, Contact, DetailPost

BASE_CONTEXT = {
    "ServiceMenu": SubCategory.objects.filter(cate_type="0"),
    "ProductMenu": SubCategory.objects.filter(cate_type="1"),
    "CTAContent": Content.objects.filter(page="0", component_type="5").first(),
    "Contact": Contact.objects.all().first(),
}


def index(request):
    context = {
        "Title": "Movento",
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
        "SliderContent": Content.objects.filter(page="0", component_type="1").first(),
        "FeatureContent": Content.objects.filter(page="0", component_type="2").first(),
        "ProductContent": Content.objects.filter(page="0", component_type="3").first(),
        "CommentTitle": Content.objects.filter(page="0", component_type="4").first(),
        "CommentContent": CustomerComment.objects.all(),
        "SubCategory": SubCategory.objects.all(),
        "DisplayServiceCategory": SubCategory.objects.filter(cate_type="0", is_homepage_content=True),
    }
    # assert False
    return render(request, 'homepage.html', {**context, **BASE_CONTEXT})


def subcategory(request, subcatename):
    subcategory_obj = SubCategory.objects.filter(code=subcatename).first()
    context = {
        "SubCategory": subcategory_obj,
        "evenlist": [i for i in range(subcategory_obj.detailsubcategory_set.all().count() + 1) if i % 2 == 0]
    }
    return render(request, 'subcategory.html', {**context, **BASE_CONTEXT})


def detailsubcategory(request, subcatename, detailsubcatename):
    detailsubcategory = DetailSubCategory.objects.filter(code=detailsubcatename).first()
    detailpost_list = detailsubcategory.detailpost_set.all()
    paginator = Paginator(detailpost_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    context = {
        "SubCategory": SubCategory.objects.filter(code=subcatename).first(),
        "DetailSubCategory": detailsubcategory,
        "DetailPosts": paginator.get_page(page),
        "OutStandingPosts": detailpost_list.filter(is_outstanding=True),
        "Advertising": Content.objects.filter(page='2', component_type='6').first(),
    }
    return render(request, 'detailsubcategory.html', {**context, **BASE_CONTEXT})


def detailpost(request, subcatename, detailsubcatename, detailpostname):
    context = {
        "SubCategory": SubCategory.objects.filter(code=subcatename).first(),
        "DetailSubCategory": DetailSubCategory.objects.filter(code=detailsubcatename).first(),
        "DetailPost": DetailPost.objects.filter(code=detailpostname).first(),
        "GridImageColumnCount": int(DetailPost.detailpostimages_set.all().count()) / 2,
    }
    return render(request, 'detailpost.html', {**context, **BASE_CONTEXT})
