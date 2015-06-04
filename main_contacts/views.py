#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a

from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
from django.core.mail import send_mail

from dva_etaja.settings import EMAIL_HOST_USER

from main_contacts.models import MainPageText, Advantages, Contacts
from main_contacts.forms import EmailForm

# Create your views here.
def index(request):
    """
    Show main pages
    :param request: request object
    :return: HttpResponse object
    """
    main_page = get_object_or_404(MainPageText, pk=1)
    advantages = get_list_or_404(Advantages)[:3]
    return render_to_response('main_contacts/index.html', {'main_page': main_page, 'advantages': advantages},
                              context_instance=RequestContext(request))


def contacts(request):
    """
    Show contacts page with feedback form
    :param request:  request object
    :return: Httpresponse object
    """
    contact = get_object_or_404(Contacts, pk=1)
    error = ''
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            client_mail = form.cleaned_data['email']
            subject = u"Сообщение с сайта Два этажа от " + client_mail
            client = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message_body = form.cleaned_data['message']
            sender = EMAIL_HOST_USER    # for debug only should use settings.EMAIL_HOST_USER
            message = subject + '\n' +  message_body + '\n' + u"Контакты: " + '\n' + client_mail \
                      + '\n' + phone + '\n' + client
            recipients = [contact.email]
            try:
                send_mail(subject, message, sender, recipients)
            except:
                error = u"Не удалось отправить сообщение"
        else:
            error = u"Ошибка при заполнении полей. Пожалуйста попробуйте снова"
    form = EmailForm()
    return render_to_response('main_contacts/contacts.html', {'contact': contact, 'error': error, 'form': form},
                                      context_instance=RequestContext(request))


def json_contacts(request):
    """
    Return contacts as JSON
    :param request: request object
    :return: Contacts object as JSON
    """
    contacts = get_object_or_404(Contacts, pk=1)
    serilized_contacts = serializers.serialize('json', [contacts], fields=('phone', 'phone_2', 'zip', 'email', 'map',
                                                                           'comments'))
    return HttpResponse(serilized_contacts, content_type='json')