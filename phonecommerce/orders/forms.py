from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):

    class Meta:

        model = Order

        fields = ['first_name', 'last_name', 'phone', 'email', 'adress_line_1',
                  'adress_line_2', 'country', 'state', 'city', 'order_note']
