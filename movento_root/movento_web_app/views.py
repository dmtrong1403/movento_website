from datetime import datetime

from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import ContactForm
from .models import *


def base_context():
    return {
        "ServiceMenu": SubCategory.objects.filter(cate_type="0"),
        "ProductMenu": ProductCategory.objects.all(),
        "CTAContent": Content.objects.filter(page="0", component_type="5").first(),
        "Contact": Contact.objects.all().first(),
        "Partners": Partner.objects.all(),
        "ContactForm": ContactForm(),
    }


def convert_string(input_string):
    output_string = str(input_string).lower().strip()
    for char in output_string:
        if char in "!@%\^*()+=<>?/,.:;\' \"&#[]~$_":
            output_string = output_string.replace(char, "-")
        elif char in "àáạảãâầấậẩẫăằắặẳẵ":
            output_string = output_string.replace(char, "a")
        elif char in "èéẹẻẽêềếệểễ":
            output_string = output_string.replace(char, "e")
        elif char in "ìíịỉĩ":
            output_string = output_string.replace(char, "i")
        elif char in "òóọỏõôồốộổỗơờớợởỡ":
            output_string = output_string.replace(char, "o")
        elif char in "ùúụủũưừứựửữ":
            output_string = output_string.replace(char, "u")
        elif char in "ỳýỵỷỹ":
            output_string = output_string.replace(char, "y")
        elif char in "đ":
            output_string = output_string.replace(char, "d")
        output_string = output_string.replace("--", "-")
    return output_string


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
        "EighthSection": Content.objects.filter(page="1", component_type="15").first(),
        "NinthSection": Content.objects.filter(page="1", component_type="16").first(),
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


def product_category(request, cate_code):
    Product_Category = ProductCategory.objects.filter(code=cate_code).first()
    Products = Product.objects.filter(category=Product_Category.id).all()
    paginator = Paginator(Products, 9)
    page = request.GET.get('page')
    LastIndex = Products.count() - 1
    if int(page) >= 2:
        LastIndex = (Products.count() % 9) - 1
    context = {
        "ProductCategory": Product_Category,
        "Products": paginator.get_page(page),
        "Tags": Product_Category.tag.all(),
        "ListCategory": ProductCategory.objects.all(),
        "LastIndex": LastIndex,
        "Openrow_Indexes": [i for i in range(0, Products.count() + 1, 3)],
        "Closerow_Indexes": [i for i in range(2, Products.count() + 1, 3)]
    }
    # assert False
    return render(request, 'product_category.html', {**context, **base_context()})


def product_detail(request, cate_code, product_code):
    product_category = ProductCategory.objects.filter(code=cate_code).first()
    prd = Product.objects.filter(code=product_code).first()
    context = {
        "ProductCategory": product_category,
        "Product": prd,
        "RelatedProducts": product_category.product_set.all(),
        "OutStandingProducts": Product.objects.filter(is_outstanding=True),
        "ListRating": [1, 2, 3, 4, 5],
        "ProductRating": int(prd.rating),
    }
    # assert False
    return render(request, 'product_detail.html', {**context, **base_context()})


def search_product(request):
    context = {
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
        "ListCategory": ProductCategory.objects.all(),
        "ResponseMessage": "Không có kết quả tìm kiếm",
    }
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        Products = Product.objects.all()
        MatchedProducts = []
        for product in Products:
            if convert_string(product.name) in convert_string(keyword) or convert_string(keyword) in convert_string(
                    product.name):
                MatchedProducts.append(product)
        if len(MatchedProducts) > 0:
            context.update({
                "ResponseMessage": "Kêt quả tìm kiếm cho từ khóa: {}".format(keyword),
                "Products": MatchedProducts,
                "LastIndex": len(MatchedProducts) - 1,
                "Openrow_Indexes": [i for i in range(0, len(MatchedProducts) + 1, 3)],
                "Closerow_Indexes": [i for i in range(2, len(MatchedProducts) + 1, 3)]
            })
    # assert False
    return render(request, 'search_product.html', {**context, **base_context()})


def search_product_tagname(request, tagname):
    context = {
        "CoverContent": Content.objects.filter(page="0", component_type="0").first(),
        "ListCategory": ProductCategory.objects.all(),
        "ResponseMessage": "Không có kết quả tìm kiếm",
    }
    Products = Product.objects.all()
    MatchedProducts = []
    for product in Products:
        isMatched = False
        for tag in product.tag.all():
            if tag.code == convert_string(tagname):
                isMatched = True
        if isMatched:
            MatchedProducts.append(product)
    if len(MatchedProducts) > 0:
        context.update({
            "ResponseMessage": "Kêt quả tìm kiếm cho liên kết: {}".format(
                Tag.objects.filter(code=tagname).first().name),
            "Products": MatchedProducts,
            "LastIndex": len(MatchedProducts) - 1,
            "Openrow_Indexes": [i for i in range(0, len(MatchedProducts) + 1, 3)],
            "Closerow_Indexes": [i for i in range(2, len(MatchedProducts) + 1, 3)]
        })
    # assert False
    return render(request, 'search_product.html', {**context, **base_context()})
