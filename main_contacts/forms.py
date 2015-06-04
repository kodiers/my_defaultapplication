#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a

from django import forms

class EmailForm(forms.Form):
    """
    Form for send messages and etc
    """
    name = forms.CharField(label=u'Имя', max_length=100)
    phone = forms.CharField(label=u'Телефон', max_length=100)
    email = forms.EmailField(label=u'Электронная почта', max_length=100)
    message = forms.CharField(widget=forms.Textarea(), label=u'Сообщение')
