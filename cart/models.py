# -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    hash = models.CharField("Хеш", max_length=200)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Корзина", null=True)
    product = models.ForeignKey(Product, verbose_name="Товар", null=True, on_delete=models.SET_NULL)

    name = models.CharField("Название", max_length=200, blank=True)
    price = models.IntegerField("Цена", blank=True)
    price_sale = models.IntegerField("Цена сос кидкой", blank=True)
    sale_status = models.BooleanField("Сделать скиду", blank=True)
    image = models.CharField("Изображение", max_length=200, blank=True)

    cart_count = models.IntegerField("Количество", blank=True)
    cart_size = models.CharField("Размер", max_length=200, blank=True)
    cart_color = models.CharField("Цвет", max_length=200, blank=True)
    cart_price = models.IntegerField("Цена при заказе", default=0)

    def create(self, product):
        self.name = product.name
        self.price = product.price
        self.price_sale = product.price_sale
        self.sale_status = product.sale_status
        self.image = product.image
        if product.sale_status:
            self.cart_price = product.price_sale
        else:
            self.cart_price = product.price
        return self
