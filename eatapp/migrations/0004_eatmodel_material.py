# Generated by Django 3.1.6 on 2021-02-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatapp', '0003_auto_20210212_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatmodel',
            name='material',
            field=models.TextField(blank=True, default='a', null=True),
        ),
    ]