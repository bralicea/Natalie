# Generated by Django 3.1 on 2020-12-31 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20201231_1813'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PortfolioImageCategorie',
            new_name='PortfolioImageCategories',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='portfolioimagecategories',
            options={'verbose_name_plural': 'PortfolioImageCategories'},
        ),
    ]
