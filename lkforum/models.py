from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core import mail

class Common(models.Model):
    created = models.DateTimeField('создан', auto_now_add=True)
    changed = models.DateTimeField('изменен', auto_now=True)
    class Meta:
        abstract = True

        
class Receiver(Common):
    user = models.ForeignKey(User, unique=True, verbose_name='Логин', related_name='receiver_profile')
    post = models.CharField('Должность', max_length=250, unique=True)
    extra_email = models.CharField('Дополнительный e-mail', max_length=250, blank=True, default='')
    class Meta:
        verbose_name = 'Адресат вопросов'
        verbose_name_plural = 'Адресаты вопросов'

    def __str__(self):
        return self.post
    def __unicode__(self):
        return self.post
        
        
class Topic(Common):
    name = models.CharField('Тема', max_length=250, unique=True)
    default_receiver = models.ForeignKey(Receiver, verbose_name='Адресат по умолчанию')
    info = models.TextField('Описание темы')
    number = models.CharField('Идентификатор темы', max_length=5, help_text='Темы с одинаковым индентификатором отображаются у пользователей сгруппированными.')
    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

        
class QnAns(Common):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True, default='')
    author = models.ForeignKey(User, verbose_name='Автор вопроса', related_name='qnans_profile')
    receiver = models.ForeignKey(Receiver, verbose_name='Автор ответа')
    topic = models.ForeignKey(Topic, verbose_name='Тема вопроса')
    is_private = models.BooleanField('Личный', default=False)
    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'        
            
    def show_author(self):
        return format_html('<a href="/admin/lkforms/userprofile/' + str(self.author.profile.all()[0].id) + '">' + self.author.profile.all()[0].sname + ' ' + self.author.profile.all()[0].name + ' ' + self.author.profile.all()[0].pname + '</a>')
    show_author.short_description = 'Автор вопроса'
    show_author.admin_order_field = 'author'
            
    def show_receiver(self):
        return format_html('<a href="/admin/lkforms/userprofile/' + str(self.receiver.user.profile.all()[0].id) + '">' + self.receiver.user.profile.all()[0].sname + ' ' + self.receiver.user.profile.all()[0].name + ' ' + self.receiver.user.profile.all()[0].pname + '</a><br>' + self.receiver.post)
    show_receiver.short_description = 'Автор ответа'
    show_receiver.admin_order_field = 'receiver'
    
    def make_receiver_email(self):        
        connection = mail.get_connection()
        msg = mail.EmailMessage('Вам задали вопрос в Личном кабинете СУНЦ МГУ', self.question + '<br><a href="http://lk.internat.msu.ru/lk/forum/answers/' + str(self.id) + '">Answer</a><br>--<br><br>This letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [self.receiver.extra_email, self.receiver.user.email])
        msg.content_subtype = "html"
        try:
            connection.send_messages([msg,])
        except Exception:           
            return 'Ваш вопрос сохранен, но отправить e-mail адресату вопроса не удалось. Пожалуйста, напишите о проблеме на lksunc@gmail.com.'
        else:
            return 'Ok! Your question №' + str(self.id)
    
    def make_author_email(self):        
        connection = mail.get_connection(use_tls = True)
        msg = mail.EmailMessage('Добавлен ответ на Ваш вопрос в Личном кабинете СУНЦ МГУ', self.question + '<br>' + self.answer + '<br><a href="http://lk.internat.msu.ru/lk/forum/my/">Show</a><br>--<br><br>This letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [self.author.email,])
        msg.content_subtype = "html"
        try:
            connection.send_messages([msg,])
        except Exception:           
            return 'Ваш ответ сохранен, но отправить e-mail автору вопроса не удалось. Пожалуйста, напишите о проблеме на lksunc@gmail.com.'
        else:
            return 'Ответ сохранен' 
            
    def __str__(self):
        return self.question
    def __unicode__(self):
        return self.question

