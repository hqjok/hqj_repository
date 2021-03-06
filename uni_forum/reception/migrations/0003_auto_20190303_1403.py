# Generated by Django 2.1.7 on 2019-03-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20190303_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_click_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_comment',
            field=models.TextField(default={}),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_lift',
            field=models.IntegerField(default=0),
        ),
    ]
