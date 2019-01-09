from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from .models import *
from datetime import datetime


def base_context():
    return {
        "ServiceMenu": SubCategory.objects.filter(cate_type="0"),
        "ProductMenu": SubCategory.objects.filter(cate_type="1"),
        "CTAContent": Content.objects.filter(page="0", component_type="5").first(),
        "Contact": Contact.objects.all().first(),
        "Partners": Partner.objects.all(),
        "ContactForm": ContactForm(),
    }


def index(request):
    context = {
        "Title": "Trang chủ",
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
        "SliderContent": Content.objects.filter(page="0", component_type="1").first(),
        "FeatureContent": Content.objects.filter(page="0", component_type="2").first(),
        "ProductContent": Content.objects.filter(page="0", component_type="3").first(),
        "CommentTitle": Content.objects.filter(page="0", component_type="4").first(),
        "CommentContent": CustomerComment.objects.all(),
        "DisplayServiceCategory": SubCategory.objects.filter(cate_type="0", is_homepage_content=True),
    }
    # assert False
    return render(request, 'homepage.html', {**context, **base_context()})


def subcategory(request, subcatename):
    subcategory_obj = SubCategory.objects.filter(code=subcatename).first()
    context = {
        "SubCategory": subcategory_obj,
        "DetailSubCategory": subcategory_obj.detailsubcategory_set.all(),
        "evenlist": [i for i in range(subcategory_obj.detailsubcategory_set.all().count() + 1) if i % 2 == 0]
    }
    return render(request, 'subcategory.html', {**context, **base_context()})


def detailsubcategory(request, subcatename, detailsubcatename):
    detailsubcategory = DetailSubCategory.objects.filter(code=detailsubcatename).first()
    detailpost_list = detailsubcategory.detailpost_set.all()
    paginator = Paginator(detailpost_list, 5)  # Show 10 contacts per page
    page = request.GET.get('page')
    detailpost_top5 = detailsubcategory.detailpost_set.filter(is_outstanding=True).order_by('-id')[:5]
    context = {
        "SubCategory": SubCategory.objects.filter(code=subcatename).first(),
        "DetailSubCategory": detailsubcategory,
        "DetailPosts": paginator.get_page(page),
        "OutStandingPosts": detailpost_top5,
        "Advertising": Content.objects.filter(page='2', component_type='6').first(),
    }
    return render(request, 'detailsubcategory.html', {**context, **base_context()})


def detailpost(request, subcatename, detailsubcatename, detailpostname):
    post = DetailPost.objects.filter(code=detailpostname).first()
    context = {
        "SubCategory": SubCategory.objects.filter(code=subcatename).first(),
        "DetailSubCategory": DetailSubCategory.objects.filter(code=detailsubcatename).first(),
        "DetailPost": post,
        "GridImageColumnCount": int(post.detailpostimages_set.all().count() / 2),
    }
    return render(request, 'detailpost.html', {**context, **base_context()})


def contact(request):
    context = {
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
    }
    return render(request, 'contact.html', {**context, **base_context()})


def about(request):
    context = {
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
        "FirstSection": Content.objects.filter(page="1", component_type="7").first(),
        "SecondSection": Content.objects.filter(page="1", component_type="8").first(),
        "ThirdSection": Content.objects.filter(page="1", component_type="9").first(),
        "FourthSection": Content.objects.filter(page="1", component_type="10").first(),
        "FifthSection": Content.objects.filter(page="1", component_type="11").first(),
        "SixthSection": Content.objects.filter(page="1", component_type="12").first(),
        "SeventhSection": Content.objects.filter(page="1", component_type="13").first(),
        "ShortDescription": Content.objects.filter(page="1", component_type="14").first(),
    }
    return render(request, 'about.html', {**context, **base_context()})


def submit_request(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = """
            Tên khách hàng: {name}
            Email: {email}
            Số điện thoại: {phone}
            Nội dung yêu cầu: {message}
            """.format(name=cd['name'], email=cd['email'], phone=cd['phone'], message=cd['message'])
            send_mail(
                'Yêu cầu tư vấn {now}'.format(now=datetime.now()),
                message,
                'noreply.movento.com.vn@gmail.com',
                ['movento.vn@gmail.com'],
                fail_silently=False,
            )
    context = {
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
    }
    return render(request, 'success.html', {**context, **base_context()})


