from django.urls import path
from landingby.views import index, order_page, feedback_page, complete_page


urlpatterns = [
    path('', index, name='index'),
    path('order_page', order_page, name='order'),
    path('feedback', feedback_page, name='feedback'),
    path('complete', complete_page, name='complete'),

]
