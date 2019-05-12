# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from lkforms.models import UserProfile

class RegistrationForm(forms.Form):

    required_css_class = 'required'

    username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, label=_(u'Логин'), error_messages={'invalid': _(u'Это поле может содержать только латинские буквы, цифры и @/./+/-/_ символы.')})
    email = forms.EmailField(label=_(u'E-mail'))
    sname = forms.CharField(label=_(u'Фамилия'))
    name = forms.CharField(label=_(u'Имя'), help_text=_(u'ФИО следует указывать в точности, как в документе, удостоверяющем личность'))
    pname = forms.CharField(label=_(u'Отчество'), help_text=_(u'если отчество отсутствует, напишите в этой графе - нет'))
    bday = forms.RegexField(regex=r'^\d{4}\-(0\d|1[012])\-([0-2]\d|3[01])$', label=_(u'Дата рождения (ГГГГ-ММ-ДД)'), error_messages={'invalid': _(u'Неверный формат даты.')})
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1, _(u'жен')),(2, _(u'муж'))], label=_(u'Пол'))
    src = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1,_(u'интернет')),(2,_(u'учитель')),(3,_(u'знакомый')),(4,_(u'email письмо')),(5,_(u'журнал "Квант"')),(6,_(u'журнал "Потенциал"')),(7,_(u'ВЗМШ')),(8,_(u'другое'))], label=_(u'Откуда Вы или Ваши родители узнали о нашем сайте?'))
    yasrc = forms.CharField(widget=forms.Textarea(), required=False, label=_(u'Если Вы выбрали "Другое", уточните, пожалуйста:'))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_(u'Пароль'))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_(u'Пароль (еще раз)'))

    def clean(self): 
	    if 'bday' in self.cleaned_data and 'sname' in self.cleaned_data and 'name' in self.cleaned_data and 'pname' in self.cleaned_data:
		    if UserProfile.objects.filter(bday__iexact=self.cleaned_data['bday']):
			    for usp in UserProfile.objects.filter(bday=self.cleaned_data['bday']):
				    if str(usp.sname.encode('utf-8')) == str(self.cleaned_data['sname'].strip().lower().title().encode('utf-8')) and str(usp.name.encode('utf-8')) == str(self.cleaned_data['name'].strip().lower().title().encode('utf-8')) and str(usp.pname.encode('utf-8')) == str(self.cleaned_data['pname'].strip().lower().title().encode('utf-8')):
					    s = 'Пользователь с данными ' + self.cleaned_data['sname'].lower().title() + ' ' + self.cleaned_data['name'].lower().title() + ' ' + self.cleaned_data['pname'].lower().title() + ' ' + str(usp.bday) + ' уже зарегистрирован. Опыт показывает, что скорее всего это Вы и есть, просто забыли о том, что регистрировались, или кто-то из Ваших родственников зарегистрировал Вас без Вашего ведома. Попробуйте воспользоваться сервисом "Восстановление пароля". Если это не поможет, то напишите в техподдержку на lksunc@gmail.com, указав в теме "двойники".'
                                            s = _(s)
					    raise forms.ValidationError(s)
	    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
		    if self.cleaned_data['password1'] != self.cleaned_data['password2']:
			    raise forms.ValidationError(_(u'Пароли не совпадают.'))
	    return self.cleaned_data
	
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_(u'Пользователь с таким email уже зарегистрирован.'))
        return self.cleaned_data['email']
		     
    def clean_username(self):     		
        if User.objects.filter(username__iexact=self.cleaned_data['username']):
            raise forms.ValidationError(_(u'Пользователь с таким логином уже существует.'))
        return self.cleaned_data['username']
