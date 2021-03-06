# Generated by Django 2.1.3 on 2018-11-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movento_web_app', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên bài viết')),
                ('avatar', models.ImageField(upload_to='post_avatar_images', verbose_name='Ảnh đại diện')),
                ('customer', models.CharField(max_length=100, verbose_name='Tên khách hàng')),
                ('address', models.CharField(max_length=100, verbose_name='Địa chỉ')),
                ('start_date', models.DateField(verbose_name='Ngày thiết kế')),
                ('code', models.SlugField(max_length=100, verbose_name='Mã bài viết')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả ngắn')),
                ('main_content', models.TextField(blank=True, null=True, verbose_name='Nội dung')),
                ('is_outstanding', models.BooleanField(default=False, verbose_name='Bài viết nổi bật ?')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movento_web_app.DetailSubCategory', verbose_name='Danh mục')),
                ('tag', models.ManyToManyField(to='movento_web_app.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Bài viết chi tiết',
                'verbose_name_plural': 'Bài viết chi tiết',
            },
        ),
        migrations.CreateModel(
            name='DetailPostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_detail_images', verbose_name='Hình ảnh')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movento_web_app.DetailPost', verbose_name='Bài viết')),
            ],
            options={
                'verbose_name': 'Hình ảnh bài viết',
                'verbose_name_plural': 'Hình ảnh bài viết',
            },
        ),
    ]
