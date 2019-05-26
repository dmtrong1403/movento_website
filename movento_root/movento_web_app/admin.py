from django.contrib import admin

from .models import *


#
# Product models
#

# class ProductAttrs_ColorAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# class ProductAttrs_MaterialAdmin(admin.ModelAdmin):
#     list_display = ('name',)


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ]
    list_display = ('category', 'name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttrs_Color)
admin.site.register(ProductAttrs_Material)


#
# Post models
#

class DetailPostImagesInline(admin.TabularInline):
    model = DetailPostImages


class DetailPostAdmin(admin.ModelAdmin):
    inlines = [DetailPostImagesInline, ]
    list_display = ('name', 'category')


# class DetailPostInline(admin.TabularInline):
#     model = DetailPost


admin.site.register(DetailPost, DetailPostAdmin)


#
# Category models
#

class DetailSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DetailSubCategory, DetailSubCategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


#
# Content models
#

class ContentImagesInline(admin.TabularInline):
    model = ContentImages


class ContentAdmin(admin.ModelAdmin):
    inlines = [ContentImagesInline, ]
    list_display = ('name', 'page', 'component_type')


admin.site.register(Content, ContentAdmin)


#
# Customer comment model
#

class CustomerCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(CustomerComment, CustomerCommentAdmin)

#
# Contact model
#

admin.site.register(Contact)

#
# Tag model
#

admin.site.register(Tag)

#
# Partner model
#

admin.site.register(Partner)


#
# Order models
#

class OrderLineInline(admin.TabularInline):
    model = OrderLine


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline, ]
    list_display = ('tag', 'customer_name', 'status', 'created_date')


admin.site.register(Order, OrderAdmin)
