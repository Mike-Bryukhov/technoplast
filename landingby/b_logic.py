"""Here we store code concerning all business logic"""

from django.forms import modelform_factory  # ModelForm
from .models import *


SupplierForm = modelform_factory(
    Supplier,
    fields=('supplier_name', 'supplier_mobile', 'supplier_email'),
    labels={'supplier_name': 'Ф.И.О.', 'supplier_mobile': 'Телефон: +380', 'supplier_email': '@mail:'},
    help_texts={'supplier_name': 'Укажите, по возможности, полное имя',
                'supplier_mobile': 'Последние девять цифр вашего номера',
                'supplier_email': 'Почта для обратной связи (не обязательно)'},
    field_classes={},
    widgets={}
)


OrderForm = modelform_factory(
    ProductOrder,
    fields=('product_type', 'product_quantity'),
    labels={'product_type': 'Вид полипропиленовой тары', 'product_quantity': 'Количество'},
    help_texts={'product_type': 'Выберите тип товара на продажу'},
    field_classes={},
    widgets={}
)
