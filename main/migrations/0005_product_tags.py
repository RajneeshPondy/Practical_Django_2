# Generated by Django 3.1.5 on 2021-01-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productname_capitalize'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.ProductTag'),
        ),
    ]