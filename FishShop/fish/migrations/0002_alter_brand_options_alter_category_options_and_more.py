# Generated by Django 4.2.2 on 2023-07-02 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['NameBrand'], 'verbose_name_plural': 'Бренд'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['NameCategory'], 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Название'},
        ),
        migrations.AlterModelOptions(
            name='undercategory',
            options={'ordering': ['NameUnderCategory'], 'verbose_name_plural': 'Под категория'},
        ),
    ]
