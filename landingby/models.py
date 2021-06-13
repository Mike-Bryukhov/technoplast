from django.db import models


class Supplier(models.Model):
    """This entity is Not intended as active 'user record' at the moment, only for database;
    supplier unique ID is implemented by framework itself.
    Boolean "markers" probably will be refactored on app owners demand"""

    supplier_name = models.CharField('Имя поставщика:', max_length=50)
    supplier_mobile = models.CharField('Телефон поставщика: +380', max_length=12)
    supplier_email = models.EmailField('@mail:', blank=True)
    supplier_status = models.BooleanField('Статус "Поставщик"', default=True)
    customer_status = models.BooleanField('Статус "Покупатель"', default=False)
    loyalty_status = models.BooleanField('Является участником программы лояльности', default=False)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}_{self.supplier_name}'


class ProductType(models.Model):
    """ It's only a simple choice of product types now.
    Probably will be refactored on owners demand in future"""
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
    """Suppose to be a 'base' for the product ordering form.
    At the moment intended to be used via admin panel by app owner for business coordination purposes
    No accountancy or "external connection" features were requested"""

    supplier_name = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Имя поставщика')
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Тип тары')
    product_quantity = models.PositiveSmallIntegerField('Количество', default=1)
    order_datetime = models.DateTimeField('Дата заказа', auto_now_add=True)
    mailing_status = models.BooleanField('Отправлено', default=False)

    class Meta:
        verbose_name = 'Заказ на продажу'
        verbose_name_plural = 'Заказы на продажу'

    def __str__(self):
        return f'Заказ №{self.pk} поставщика {self.supplier_name} от {self.order_datetime}'
