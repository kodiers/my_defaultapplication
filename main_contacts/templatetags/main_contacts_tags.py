#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a

from django import template
from main_contacts.models import Contacts

register = template.Library()

@register.simple_tag()
def contact_email():
    """
    :return: contacts email address
    """
    contact = Contacts.objects.get(pk=1)
    return contact.email

@register.simple_tag()
def contact_phone():
    """
    :return: contacts phone address
    """
    contact = Contacts.objects.get(pk=1)
    return contact.phone

@register.simple_tag()
def contact_address():
    """
    :return: string with contacts zip and address
    """
    contact = Contacts.objects.get(pk=1)
    return contact.zip + ' ' + contact.address


@register.simple_tag()
def businessdays():
    """
    :return: string with business days
    """
    contact = Contacts.objects.get(pk=1)
    return contact.businessdays

