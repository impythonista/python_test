import uuid
from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    """
        This model is used to save, update and gather the basic information
        which are listed below like name, address, email, phone number etc.
        of the clients.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Client Name"))
    street_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=
                _("Street Name"))
    suburb = models.CharField(max_length=50, null=True, blank=True, verbose_name=
                _("Suburb"))
    postcode = models.CharField(max_length=10, null=True, blank=True, verbose_name=
                _("Postcode"))
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name=
                _("State"))
    contact_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=
                _("Contact Name"))
    email = models.EmailField(max_length=70, unique=True, verbose_name=_("Email"))
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)
