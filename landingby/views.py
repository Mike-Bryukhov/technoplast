import re
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import OrderForm


def index(request):
    return render(request, 'landingby/index.html')


def order_page(request):
    error_message = ''
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid() and order_form.is_valid():
            order_form.save(commit=False)

            '''Placeholder for regex cleaning of 'name' field'''

            '''some more regex cleaning'''
            supplier_mob = order_form.cleaned_data['supplier_mobile']
            supplier_stripped_mob = re.findall(r'[0\d_\-\d]{12}$', supplier_mob)
            order_form.cleaned_data['supplier_mobile'] = supplier_stripped_mob

            '''Placeholder for regex cleaning of 'email' field'''

            order_form.save(commit=True)
            return redirect('complete')
        else:
            error_message = 'Ошибка: Введенные данные некоррктны'

    order_form = OrderForm()
    order_data = {
        'order_data': order_form,
        'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY,
        'error': error_message,
    }
    return render(request, 'landingby/order_page.html', order_data)


def complete_page(request):
    return render(request, 'landingby/complete.html')
