from django.contrib import admin

from .models import *


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
    # inlines = [DetailPostInline, ]
    list_display = ('name', 'description')


# class DetailSubCategoryInline(admin.TabularInline):
#     model = DetailSubCategory


class SubCategoryAdmin(admin.ModelAdmin):
    # inlines = [DetailSubCategoryInline, ]
    list_display = ('name', 'description')


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DetailSubCategory, DetailSubCategoryAdmin)


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