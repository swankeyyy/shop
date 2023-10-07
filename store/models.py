from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='brand_name')
    description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Brand_URL"
    )

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("brand", kwargs={"brand_slug": self.slug})

    class Meta:
        verbose_name = "Бренд"


class UseFor(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='used_for')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="pro_or_home_URL")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("usefor", kwargs={"brand_slug": self.slug})

    class Meta:
        verbose_name = "Назначение"


class ElectroType(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='electro_type')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("type", kwargs={"brand_slug": self.slug})

    class Meta:
        verbose_name = "Тип"


class SubCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("subcategory", kwargs={"brand_slug": self.slug})

    class Meta:
        verbose_name = "Подкатегория"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")
    description = models.TextField(max_length=300, null=True, blank=True)
    subcategory = models.ManyToManyField(SubCategory)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("category", kwargs={"brand_slug": self.slug})

    class Meta:
        verbose_name = "Основная категория"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название товара")
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд', null=True, blank=True)
    usefor = models.ForeignKey(UseFor, on_delete=models.PROTECT, verbose_name='Назначение', null=True, blank=True)
    electrotype = models.ForeignKey(ElectroType, on_delete=models.PROTECT, verbose_name='Тип', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("product", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Список товаров"
        ordering = ["time_create", "title"]
