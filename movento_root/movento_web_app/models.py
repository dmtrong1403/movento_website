from django.db import models
from datetime import date


#
# Category models
#


class SubCategory(models.Model):
    CATE_TYPE = (
        ('0', 'Dịch vụ'),
        ('1', 'Sản phẩm')
    )

    COLUMN_TYPE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    cate_type = models.CharField(max_length=20, choices=CATE_TYPE, verbose_name="Loại danh mục")
    description = models.TextField("Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh")
    is_homepage_content = models.BooleanField("Hiển thị ở mục giới thiệu ?", default=True)
    column_type = models.CharField(max_length=20, choices=COLUMN_TYPE, verbose_name="Số cột hiển thị")
    code = models.SlugField(max_length=100, verbose_name="Mã danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 1"
        verbose_name_plural = "Danh mục cấp 1"

    def __str__(self):
        return str(self.name)


class DetailSubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = models.TextField("Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh")
    parent_cate = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="Danh mục cha")
    is_homepage_content = models.BooleanField("Hiển thị ở mục giới thiệu ?", default=True)
    code = models.SlugField(max_length=100, verbose_name="Mã danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 2"
        verbose_name_plural = "Danh mục cấp 2"

    def __str__(self):
        return str(self.name)


#
# Content models
#


class Content(models.Model):
    COMPONENT_TYPE = (
        ('0', 'Cover'),
        ('1', 'Slide ảnh giới thiệu'),
        ('2', 'Dịch vụ cung cấp'),
        ('3', 'Công trình tiêu biểu'),
        ('4', 'Nhận xét khách hàng'),
        ('5', 'Call to action'),
        ('6', 'Quảng cáo')
    )

    PAGE_TYPE = (
        ('0', 'Trang chủ'),
        ('1', 'Giới thiệu'),
        ('2', 'Danh mục cấp 2')
    )
    name = models.CharField(max_length=100, verbose_name="Tên nội dung")
    page = models.CharField(max_length=20, choices=PAGE_TYPE, verbose_name="Trang")
    component_type = models.CharField(max_length=20, choices=COMPONENT_TYPE, verbose_name="Bộ phận")
    title = models.CharField(blank=True, null=True, max_length=100, verbose_name="Tiêu đề")
    description = models.TextField(blank=True, null=True, verbose_name="Nội dung")

    class Meta:
        verbose_name = "Nội dung trang"
        verbose_name_plural = "Nội dung trang"

    def __str__(self):
        return self.name


class ContentImages(models.Model):
    image = models.ImageField(upload_to='content_images', verbose_name="Hình ảnh")
    content = models.ForeignKey(Content, blank=True, null=True, on_delete=models.CASCADE,
                                verbose_name="Nội dung")

    class Meta:
        verbose_name = "Hình ảnh nội dung"
        verbose_name_plural = "Hình ảnh nội dung"

    def __str__(self):
        return str(self.id)


#
# Tag models
#

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên tag")
    path = models.CharField(max_length=100, verbose_name="Đường dẫn")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"

    def __str__(self):
        return str(self.name)


#
# Post models
#

class DetailPost(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên bài viết")
    avatar = models.ImageField(upload_to='post_avatar_images', verbose_name="Ảnh đại diện")
    category = models.ForeignKey(DetailSubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="Danh mục")
    tag = models.ManyToManyField(Tag, verbose_name="Tags")
    customer = models.CharField(max_length=100, verbose_name="Tên khách hàng")
    address = models.CharField(max_length=100, verbose_name="Địa chỉ")
    start_date = models.DateField(verbose_name="Ngày thiết kế")
    code = models.SlugField(max_length=100, verbose_name="Mã bài viết")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả ngắn")
    main_content = models.TextField(blank=True, null=True, verbose_name="Nội dung")
    is_outstanding = models.BooleanField(default=False, verbose_name="Bài viết nổi bật ?")

    class Meta:
        verbose_name = "Bài viết chi tiết"
        verbose_name_plural = "Bài viết chi tiết"

    def __str__(self):
        return str(self.name)


class DetailPostImages(models.Model):
    image = models.ImageField(upload_to='post_detail_images', verbose_name="Hình ảnh")
    post = models.ForeignKey(DetailPost, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name="Bài viết")

    class Meta:
        verbose_name = "Hình ảnh bài viết"
        verbose_name_plural = "Hình ảnh bài viết"

    def __str__(self):
        return str(self.id)


#
# Partner models
#

class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên đối tác")
    web = models.URLField(blank=True, verbose_name="Link web")
    image = models.ImageField(upload_to='partner_images', verbose_name="Hình ảnh")

    class Meta:
        verbose_name = "Đối tác"
        verbose_name_plural = "Đối tác"

    def __str__(self):
        return str(self.name)


#
# Customer models
#

class CustomerComment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên khách hàng")
    image = models.ImageField(upload_to='content_images', verbose_name="Hình ảnh")
    description = models.TextField(blank=True, null=True, verbose_name="Nội dung")

    class Meta:
        verbose_name = "Nhận xét khách hàng"
        verbose_name_plural = "Nhận xét khách hàng"

    def __str__(self):
        return str(self.name)


#
# Contact models
#

class Contact(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Tên công ty")
    tel = models.CharField(max_length=100, verbose_name="Tel")
    mobile = models.CharField(max_length=100, verbose_name="Mobile")
    email = models.CharField(max_length=100, verbose_name="Email")
    showroom = models.TextField(verbose_name="Showroom & office")
    factory = models.TextField(verbose_name="Xưởng")

    class Meta:
        verbose_name = "Thông tin liên hệ"
        verbose_name_plural = "Thông tin liên hệ"

    def __str__(self):
        return str(self.company_name)