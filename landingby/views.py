import re

from django.shortcuts import render, redirect
from .forms import OrderForm, SupplierForm


def index(request):
    return render(request, 'landingby/index.html')


def order_page(request):
    error_message = ''
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('feedback')  # Куда проваливаются отсюда?
        else:
            error_message = 'Ошибка: Введенные данные некоррктны'

    order_form = OrderForm()
    order_data = {
        'order_data': order_form,
        'error': error_message
    }
    return render(request, 'landingby/order_page.html', order_data)


def feedback_page(request):
    error_message = ''
    if request.method == 'POST':
        supplier_feedback = SupplierForm(request.POST)
        pure_phone_number = re.findall(r'\d-{12,12}', supplier_feedback.supplier_mobile())
        supplier_fb_clean_mob = supplier_feedback.supplier_mobile(pure_phone_number)
        if supplier_fb_clean_mob.is_valid():
            supplier_fb_clean_mob.save()
            return redirect('complete')
        else:
            error_message = 'Ошибка: Введенные данные некоррктны'

    supplier_feedback = SupplierForm()
    form_for_feedback = {
        'form_for_feedback': supplier_feedback,
        'error': error_message,
    }
    return render(request, 'landingby/feedback.html', form_for_feedback)


def complete_page(request):
    return render(request, 'landingby/complete.html')
