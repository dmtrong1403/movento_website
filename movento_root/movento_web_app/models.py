from django.db import models
from django.urls import reverse
from froala_editor.fields import FroalaField


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
    cate_type = models.CharField(max_length=20, choices=CATE_TYPE, verbose_name="Loại danh mục", default='0')
    description = models.TextField("Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh đại diện")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    is_homepage_content = models.BooleanField("Hiển thị ở mục giới thiệu ?", default=True)
    column_type = models.CharField(max_length=20, choices=COLUMN_TYPE, verbose_name="Số cột hiển thị")
    code = models.SlugField(max_length=100, verbose_name="Mã danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 1"
        verbose_name_plural = "Danh mục cấp 1"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("service_subcategory", args=[self.code, ])


class DetailSubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = models.TextField("Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh đại diện")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    parent_cate = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="Danh mục cha")
    code = models.SlugField(max_length=100, verbose_name="Mã danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 2"
        verbose_name_plural = "Danh mục cấp 2"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("service_detailsubcategory", args=[self.parent_cate.code, self.code])


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
        ('7', 'Giới thiệu chung về công ty'),
        ('8', 'Quá trình thành lập và phát triển'),
        ('9', 'Cơ sở vật chất'),
        ('10', 'Ngành nghề kinh doanh'),
        ('11', 'Các dự án đã thực hiện'),
        ('12', 'Tầm nhìn & sứ mệnh, giá trị cốt lõi'),
        ('13', 'Cơ sở pháp lý'),
        ('14', 'Giới thiệu chung'),
        ('15', 'Năng lực kinh nghiệm'),
        ('16', 'Ban lãnh đạo tổ chức'),
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
    description = FroalaField(blank=True, null=True, verbose_name="Nội dung")

    class Meta:
        verbose_name = "Nội dung trang"
        verbose_name_plural = "Nội dung trang"

    def __str__(self):
        return self.name


class ContentImages(models.Model):
    image = models.ImageField(upload_to='content_images', verbose_name="Hình ảnh")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh", default="")
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
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    category = models.ForeignKey(DetailSubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="Danh mục")
    tag = models.ManyToManyField(Tag, verbose_name="Tags")
    customer = models.CharField(max_length=100, verbose_name="Tên khách hàng")
    address = models.CharField(max_length=100, verbose_name="Địa chỉ")
    start_date = models.DateField(verbose_name="Ngày thiết kế")
    code = models.SlugField(max_length=100, verbose_name="Mã bài viết")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả ngắn")
    main_content = FroalaField(default="")
    is_outstanding = models.BooleanField(default=False, verbose_name="Bài viết nổi bật ?")

    class Meta:
        verbose_name = "Bài viết chi tiết"
        verbose_name_plural = "Bài viết chi tiết"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        detail_subcategory = DetailSubCategory.objects.get(pk=self.category.id)
        subcategory = SubCategory.objects.get(pk=detail_subcategory.parent_cate.id)
        return reverse("service_detailpost", args=[subcategory.code, detail_subcategory.code, self.code])


class DetailPostImages(models.Model):
    image = models.ImageField(upload_to='post_detail_images', verbose_name="Hình ảnh")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh", default="")
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
    image = models.ImageField(upload_to='partner_images', verbose_name="Hình ảnh đại diện")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")

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
    image = models.ImageField(upload_to='content_images', verbose_name="Hình ảnh đại diện")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
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


#
# Product models
#

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = models.TextField("Mô tả")
    is_homepage_content = models.BooleanField("Hiển thị ở mục giới thiệu ?", default=True)
    code = models.SlugField(max_length=100, verbose_name="Mã danh mục")

    class Meta:
        verbose_name = "Danh mục sản phẩm"
        verbose_name_plural = "Danh mục sản phẩm"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("product_category", args=[self.code, ])


class Product(models.Model):
    RATING = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    name = models.CharField(max_length=100, verbose_name="Tên sản phẩm")
    avatar = models.ImageField(upload_to='post_avatar_images', verbose_name="Ảnh đại diện")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    category = models.ForeignKey(ProductCategory, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="Danh mục")
    tag = models.ManyToManyField(Tag, verbose_name="Tags")
    material = models.CharField(verbose_name="Vật liệu", max_length=100, null=True)
    color = models.CharField(verbose_name="Màu sắc", max_length=100, null=True)
    rating = models.CharField(verbose_name="Đánh giá", choices=RATING, max_length=1, null=True)
    price = models.FloatField(verbose_name="Giá niêm yết", blank=True, null=True)
    discount = models.FloatField(verbose_name="Giảm giá %", blank=True, null=True)
    actual_price = models.FloatField(verbose_name="Giá cuối")
    code = models.SlugField(max_length=100, verbose_name="Mã sản phẩm")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả ngắn")
    main_content = FroalaField(default="Mô tả chi tiết")
    is_outstanding = models.BooleanField(default=False, verbose_name="Sản phẩm nổi bật ?")

    class Meta:
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Sản phẩm"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        detail_subcategory = DetailSubCategory.objects.get(pk=self.category.id)
        subcategory = SubCategory.objects.get(pk=detail_subcategory.parent_cate.id)
        return reverse("product_detail", args=[subcategory.code, detail_subcategory.code, self.code])


class ProductImages(models.Model):
    image = models.ImageField(upload_to='product_detail_images', verbose_name="Hình ảnh")
    image_alt = models.CharField(max_length=100, verbose_name="Mô tả ảnh", default="")
    post = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name="Sản phẩm")

    class Meta:
        verbose_name = "Hình ảnh sản phẩm"
        verbose_name_plural = "Hình ảnh sản phẩm"

    def __str__(self):
        return str(self.id)
