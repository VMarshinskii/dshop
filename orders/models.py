# -*- coding: utf-8 -*-
from django.db import models
from account.models import User
from cart.models import CartProduct


STATUSES = (
    (0, "В обработке"),
    (1, "Ждёт оплаты"),
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
    sum = models.IntegerField("Сумма заказа", default=0)
    status = models.IntegerField("Статус заказа", choices=STATUSES)

    first_name = models.CharField("Имя", max_length=200, default="")
    patronymic = models.CharField("Отчество", max_length=200, default="")
    last_name = models.CharField("Фамилия", max_length=200, default="")
    email = models.CharField("Email", max_length=200, default="")
    phone = models.CharField("Телефон", max_length=200, default="")
    region = models.CharField("Область", max_length=200, default="")
    city = models.CharField("Город", max_length=200, default="")
    index = models.CharField("Индекс", max_length=200, default="")
    address = models.TextField("Адрес", default="")

    delivery = models.CharField("Доставка", max_length=200, default="")
    delivery_price = models.IntegerField("Стоимость доставки")

    date_create = models.DateField("Дата создания заказа", auto_now_add=True)
    date_now = models.DateField("Дата редактирования", auto_now=True)

    products = models.ManyToManyField(CartProduct, verbose_name="Товары", blank=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class DeliveryType(models.Model):
    title = models.CharField("Название", max_length=200)
    price = models.IntegerField("Стоиомость", default=0)
    description = models.CharField("Описание", max_length=200, default="")

    class Meta:
        verbose_name = "Тип доставки"
        verbose_name_plural = "Типы доставки"

    def __unicode__(self):
        return self.title


class OrderPhone(models.Model):
    name = models.CharField("Имя", max_length=250)
    phone = models.CharField("Телефон", max_length=250)
    date = models.DateField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Заказанный звоной"
        verbose_name_plural = "Заказанные звонки"

    def __unicode__(self):
        return self.name + " : " + self.phone