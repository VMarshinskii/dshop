# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import get_template
from account.models import User
from cart.models import CartProduct
from django.template import Context


STATUSES = (
    (0, "В обработке"),
    (1, "Принят"),
    (2, "Ждёт оплаты"),
    (3, "Доставлен"),
    (4, "Отменён"),
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
    sum = models.IntegerField("Сумма заказа", default=0)
    status = models.IntegerField("Статус заказа", choices=STATUSES)

    first_name = models.CharField("Имя", max_length=200, default="")
    patronymic = models.CharField("Отчество", max_length=200, default="", blank=True)
    last_name = models.CharField("Фамилия", max_length=200, default="")
    email = models.CharField("Email", max_length=200, default="")
    phone = models.CharField("Телефон", max_length=200, default="")
    region = models.CharField("Область", max_length=200, default="", blank=True)
    city = models.CharField("Город", max_length=200, default="", blank=True)
    index = models.CharField("Индекс", max_length=200, default="")
    address = models.TextField("Адрес", default="")
    metro = models.CharField("Метро", max_length=200, default="", blank=True)

    delivery = models.CharField("Доставка", max_length=200, default="")
    delivery_price = models.IntegerField("Стоимость доставки")

    date_create = models.DateField("Дата создания заказа", auto_now_add=True)
    date_now = models.DateField("Дата редактирования", auto_now=True)

    products = models.ManyToManyField(CartProduct, verbose_name="Товары", blank=True)

    admin_comment = models.TextField("Комментарий администратора", null=True, editable=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        try:
            old_order = Order.objects.get(id=self.id)
            if old_order.status != self.status:
                t = get_template('create_order_sender.html')
                html_content = t.render(Context({
                    'hello': 'Обновлён статус заказа на <a href="http://darya-shop.ru">darya-shop.ru</a>!',
                    'user_active': True,
                    'order': self,
                    'order_status': STATUSES[self.status].encode('utf-8'),
                    'products': self.products.all(),
                }))

                msg = EmailMultiAlternatives("Обновлён статус заказа на Darya-Shop", html_content, "daryashop112@gmail.com", [self.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
        except Order.DoesNotExist:
            pass

        super(Order, self).save(*args, **kwargs)


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