# Generated by Django 3.2.9 on 2021-11-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20211115_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper_comment',
            name='paper_name',
            field=models.CharField(max_length=1024, null=True, verbose_name='paper name'),
        ),
    ]