from django import forms
from .models import ProductOrder, ProductType


class OrderForm(forms.ModelForm):
    supplier_name = forms.CharField(max_length=50, min_length=2, required=True,
                                    widget=forms.widgets.TextInput(attrs={'class': 'form',
                                                                          'placeholder': 'Как к вам обращаться?'}))
    supplier_mobile = forms.CharField(max_length=12, min_length=12, required=True,
                                      widget=forms.widgets.TextInput(attrs={'class': 'form',
                                                                            'placeholder': '050123456789'}))
    supplier_email = forms.EmailField(required=False, widget=forms.widgets.EmailInput(attrs={'class': 'form',
                                                                             'placeholder': 'адрес @-mail'}))
    product_type = forms.ModelChoiceField(queryset=ProductType.objects.all(),
                                          widget=forms.widgets.Select(attrs={'class': 'form'}))
    product_quantity = forms.IntegerField(min_value=0, max_value=100000,
                                          widget=forms.widgets.NumberInput(attrs={'class': 'form'}))

    class Meta:
        model = ProductOrder
        fields = {'supplier_name', 'supplier_mobile', 'supplier_email', 'product_type', 'product_quantity'}
