# Generated by Django 4.1.7 on 2023-04-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='blog.category'),
        ),
    ]
