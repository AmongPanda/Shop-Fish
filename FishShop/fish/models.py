from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    NameCategory = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name_plural = "Категория"
        ordering = ['NameCategory']
    def __str__(self):
        return str(self.NameCategory)

class UnderCategory(models.Model):
    NameUnderCategory = models.CharField(max_length=50, verbose_name="Под категория")

    class Meta:
        verbose_name_plural = "Под категория"
        ordering = ['NameUnderCategory']
    def __str__(self):
        return str(self.NameUnderCategory)

class Brand(models.Model):
    NameBrand = models.CharField(max_length=25, verbose_name="Бренд")

    class Meta:
        verbose_name_plural = "Бренд"
        ordering = ['NameBrand']
    def __str__(self):
        return str(self.NameBrand)

class Product(models.Model):
    CategoryProduct = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория")
    UnderCategoryProduct = models.ForeignKey(UnderCategory, on_delete=models.CASCADE, null=True, verbose_name="Под категория")
    Photo = models.ImageField(upload_to='images/', verbose_name="Фото")
    Name = models.CharField(max_length=50, verbose_name="Название продукта")
    Price = models.IntegerField(validators=[MinValueValidator(0)], null=True, max_length=50, verbose_name="Цена")
    Description = models.TextField(max_length=500, verbose_name="Описание")
    BrandProduct = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, verbose_name="Бренд")

    class Meta:
        verbose_name_plural = "Продукт"
        ordering = ['Name']
    def __str__(self):
        return str(self.Name)