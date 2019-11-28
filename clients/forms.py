from django import forms
from django.forms import ModelForm
from .models import Client


class ClientsForm(ModelForm):
  """
    This class is used to create an input form based on the fields that are listed
    below.So that the user can add a new client and update data of any existing client.
  """

  class Meta:
    model = Client
    fields = ['name', 'street_name', 'suburb', 'postcode',
        'state', 'contact_name', 'email', 'phone_number']
