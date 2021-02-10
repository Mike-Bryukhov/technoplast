from django.db import models
''' Возможно надо будет пересмотреть механики вокруг булевых "маркеров". '''


class Supplier(models.Model):
    """This entity is Not intended as active user at the moment, only for database records;
    supplier unique ID is implemented by framework itself"""

    """ Спросить про желаемую сортировку !!!!!! """
    supplier_name = models.CharField('Имя поставщика:', max_length=50)
    supplier_mobile = models.PositiveIntegerField('Телефон поставщика: +380')  # длинна номера?
    supplier_email = models.EmailField('@mail:')  # нужна валидация самой записи ч-з регулярки.
    supplier_status = models.BooleanField('Статус "Поставщик"', default=True)
    customer_status = models.BooleanField('Статус "Покупатель"', default=False)
    loyalty_status = models.BooleanField('Является участником программы лояльности', default=False)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}_{self.supplier_name}'  # for visual representation at the admin site part


class ProductType(models.Model):
    """  """
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


'''At the moment there's no need for separate measuring units, but that must be requested later'''
# class Measure(models.Model):
#     UNITS = (
#         ('кг', 'кг'),
#         ('шт', 'шт'),
#         ('упаковка', 'упаковка')
#     )
#     units = models.CharField('Единицы измерения', max_length=15, choices=UNITS)
#
#     class Meta:
#         verbose_name = 'Единицы измерения'
#         verbose_name_plural = 'Единицы измерения'
#
#     def __str__(self):
#         return self.units


class ProductOrder(models.Model):
    """Suppose to be a base for product ordering form"""
    supplier_name = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Имя поставщика')
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Тип тары')
    product_quantity = models.PositiveSmallIntegerField('Количество', default=1)
    # units_type = models.ForeignKey(Measure, on_delete=models.PROTECT, verbose_name='Единицы измерения')
    order_datetime = models.DateTimeField(auto_now_add=True)
    mailing_status = models.BooleanField('Отправлено', default=False)

    class Meta:
        verbose_name = 'Заказ на продажу'
        verbose_name_plural = 'Заказы на продажу'

    def __str__(self):
        return f'Заказ №{self.pk} поставщика {self.supplier_name} от {self.order_datetime}'
