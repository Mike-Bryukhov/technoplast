from django import forms
from .models import Supplier, ProductOrder, ProductType


class SupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(max_length=50, min_length=2, required=True,
                                    widget=forms.widgets.TextInput(attrs={'class': 'form',
                                                                          'placeholder': 'Как к вам обращаться?'}))
    supplier_mobile = forms.CharField(max_length=12, min_length=12, required=True,
                                      widget=forms.widgets.TextInput(attrs={'class': 'form',
                                                                            'placeholder': '050123456789'}))
    supplier_email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'class': 'form',
                                                                             'placeholder': 'адрес @-mail'}))

    class Meta:
        model = Supplier
        fields = {'supplier_name', 'supplier_mobile', 'supplier_email'}
        labels = {'supplier_name': 'Ф.И.О.',
                  'supplier_mobile': 'Телефон: +38',
                  'supplier_email': '@mail:'}


class OrderForm(forms.ModelForm):
    product_type = forms.ModelChoiceField(queryset=ProductType.objects.all(),
                                          widget=forms.widgets.Select(attrs={'class': 'form'}))
    product_quantity = forms.IntegerField(widget=forms.widgets.NumberInput(attrs={'class': 'form'}))

    class Meta:
        model = ProductOrder
        fields = {'product_type', 'product_quantity'}
        labels = {'product_type': 'Вид полипропиленовой тары',
                  'product_quantity': 'Количество'}
