from django.db import models


class ProductType(models.Model):
    """ It's only a simple choice of product types now.
    May be refactored on demand in future"""
    PRODUCT_CHOICES = [
        ('мешки, кг', 'Мешки - кг'),
        ('ящики, шт', 'Ящики - шт'),
        ('ящики, кг', 'Ящики - кг'),
    ]
    prod_type = models.CharField('Тип тары', max_length=15, choices=PRODUCT_CHOICES)

    class Meta:
        verbose_name = 'Тип тары'
        verbose_name_plural = 'Типы тары'

    def __str__(self):
        return self.prod_type


class ProductOrder(models.Model):
    """At the moment intended to be used via admin panel
    by app owner for business coordination purposes"""

    supplier_name = models.CharField('Имя', max_length=50)
    supplier_mobile = models.CharField('Телефон', max_length=12)
    supplier_email = models.EmailField('@-email', blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Тип тары')
    product_quantity = models.PositiveSmallIntegerField('Количество', default=1)
    order_datetime = models.DateTimeField('Дата заказа', auto_now_add=True)
    mailing_status = models.BooleanField('Отправлено', default=False)

    class Meta:
        verbose_name = 'Заказ на продажу'
        verbose_name_plural = 'Заказы на продажу'
        ordering = ['order_datetime']

    def __str__(self):
        return f'Заказ №{self.pk} поставщика {self.supplier_name, self.supplier_mobile} от {self.order_datetime}'
