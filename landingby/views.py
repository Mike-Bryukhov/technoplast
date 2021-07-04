# import re
from django.shortcuts import render, redirect

from .forms import OrderForm


def index(request):
    return render(request, 'landingby/index.html')


def order_page(request):
    error_message = ''
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid() and order_form.is_valid():
            order_form.save()
            return redirect('complete')
        else:
            error_message = 'Ошибка: Введенные данные некоррктны'

    order_form = OrderForm()
    order_data = {
        'order_data': order_form,
        'error': error_message,
    }
    return render(request, 'landingby/order_page.html', order_data)


# def feedback_page(request):  # Not used at the moment. Plan to work out regular expressions implementation
#     error_message = ''
#     if request.method == 'POST':
#         supplier_feedback = SupplierForm(request.POST)
#
#         phone_numbers_only = re.findall(r'0\d{11}$', supplier_feedback.supplier_mobile)
#         supplier_feedback.supplier_mobile() = phone_numbers_only
        #
        # if supplier_feedback.is_valid():
        #     supplier_feedback.save()
        #     return redirect('complete')
        # else:
        #     error_message = 'Ошибка: Введенные данные некоррктны'
    #
    # supplier_feedback = SupplierForm()
    # form_for_feedback = {
    #     'form_for_feedback': supplier_feedback,
    #     'error': error_message,
    # }
    # return render(request, 'landingby/feedback.html', form_for_feedback)


def complete_page(request):
    return render(request, 'landingby/complete.html')
