# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from djangosphinx.models import SphinxSearch


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    public = models.BooleanField("Опубликовать", default=True)
    parent = models.ForeignKey("self", verbose_name="Родительская категория", blank=True, null=True, default="-1")
    text = RedactorField(verbose_name="Описание",
                         redactor_options={'upload_to': 'static/uploads', 'clipboardImageUpload ': 'true',
                                           'multipleImageUpload': 'true',}, blank=True)
    url = models.CharField("Url", max_length=200, unique=True)
    description = models.CharField("Description", max_length=200, blank=True)
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True)
    step = models.IntegerField("Вложенность", blank=True)
    sort = models.IntegerField(verbose_name="Сортировка", default=0)

    class Meta:
        verbose_name_plural = u"Категории"
        verbose_name = u"Категория"

    def __unicode__(self):
        return self.title

    def get_all_product(self):
        mass_product = []

        def rec_category(obj):
            product = Product.objects.filter(public=True, category=obj)
            for product in product:
                mass_product.append(product)
            categories = Category.objects.filter(public=True, parent=obj)
            for category in categories:
                rec_category(category)

        rec_category(self)
        return reversed(sorted(mass_product, key=lambda x: x.sort))

    def get_path_categ(self):
        mass_pass = []

        def rec_path(obj):
            if obj is not None:
                mass_pass.append(obj)
                rec_path(obj.parent)

        rec_path(self)
        return mass_pass

    # проверка: является ли категория отображаемой (вклюая родительские)
    def public_check(self):
        if not self.public:
            return False
        if self.parent is None:
            return self.public
        return self.parent.public_check()

    def admin_sort(self):
        return '<span class="admin_sort" id="' + str(self.id) + '" sort_value="' + str(self.sort) + '"></span>'
    admin_sort.allow_tags = True
    admin_sort.short_description = ''


class Color(models.Model):
    title = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name_plural = "Цвета"
        verbose_name = "Цвет"

    def __unicode__(self):
        return self.title


class Model(models.Model):
    title = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name_plural = "Модели"
        verbose_name = "Модель"

    def __unicode__(self):
        return self.title


MARKET = (
    (0, '----'),
    (1, 'Хит'),
    (2, 'Новинка'),
    (3, 'Акция'),
    (4, 'Распродажа'),
    (5, 'Товар дня'),
    (6, 'Товар недели'),
    (7, 'Товар месяца'),
    (8, 'Хит сезона'),
)

PRODUCT_STATUS = (
    (0, 'Есть на складе'),
    (1, 'Ожидает поставки'),
    (2, 'Распродано'),
    (3, 'Под заказ'),
)


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    price = models.IntegerField("Цена")
    price_sale = models.IntegerField("Цена со скидкой", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True)
    sale = models.IntegerField("Скидка, %", blank=True, default=0)
    sale_status = models.BooleanField("Сделать скидку", default=False)
    count_status = models.BooleanField("Под заказ", default=False)
    product_status = models.IntegerField("Статус наличия", default=0, choices=PRODUCT_STATUS)
    count = models.IntegerField("Товар в наличии", null=True, blank=True)
    status = models.IntegerField("Рекламные метки", default=0, choices=MARKET)
    brand = models.CharField(verbose_name="Производитель", max_length=250, blank=True)
    text = RedactorField(verbose_name="Описание", redactor_options={'upload_to': 'static/uploads'}, blank=True)
    color = models.ManyToManyField(Color, verbose_name="Цвет", max_length=200, blank=True)
    model = models.ManyToManyField(Model, verbose_name="Модель", max_length=200, blank=True)
    size = models.CharField("Размер", max_length=200, blank=True)
    structure = models.CharField("Состав", max_length=200, blank=True)
    keywords = models.CharField("Ключевые слова", max_length=200)
    description = models.CharField("Description", max_length=200)
    images = models.TextField(blank=True)
    image = models.CharField(max_length=200, blank=True)
    related_products = models.ManyToManyField("self", verbose_name="Сопутствующие товары", max_length=200, blank=True)
    home_status = models.BooleanField("На главной")
    sort = models.CharField("Сортировка", max_length=200, default='')
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    popularity = models.IntegerField(verbose_name="Популярность", default=0)
    public = models.BooleanField("Опубликовать", default=True)

    search = SphinxSearch(
        index='product',
        weights={
            'name': 100,
            'keywords': 90,
            'text': 80,
        }
    )

    class Meta:
        verbose_name_plural = u"Товары"
        verbose_name = u"Товар"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.sort:
            self.sort = "{0:0=12}".format(int(self.id))
            self.save()

    def get_price(self):
        if self.sale_status:
            return self.price_sale
        return self.price

    def admin_sort(self):
        return '<span class="admin_sort" id="' + str(self.id) + '" sort_value="' + str(self.sort) + '"></span>'

    admin_sort.allow_tags = True
    admin_sort.short_description = ''


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", null=True, blank=True)
    code = models.TextField("Код видео", null=True, blank=True)
    video = models.FileField(verbose_name="Видео файл", upload_to="static/video", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Видео для товаров"
        verbose_name = "Видео для товара"
