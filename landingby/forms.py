from django import forms
from .models import *


class SupplierForm(forms.ModelForm):
    supplier_name = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'form'}))
    supplier_mobile = forms.IntegerField(widget=forms.widgets.NumberInput(attrs={'class': 'form'}))
    supplier_email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'class': 'form'}))

    class Meta:
        model = Supplier
        fields = {'supplier_name', 'supplier_mobile', 'supplier_email'}
        labels = {'supplier_name': 'Ф.И.О.',
                  'supplier_mobile': 'Телефон: +380',
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
