# Generated by Django 4.0.5 on 2022-06-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_posts_com_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='com_count',
            field=models.IntegerField(default=0, max_length=255),
        ),
    ]
