from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import User, Group
from lkforms.models import Question, Form, Theme
from django.core.urlresolvers import reverse

class Common(models.Model):
    created = models.DateTimeField('создан', auto_now_add=True)
    changed = models.DateTimeField('изменен', auto_now=True)
    class Meta:
        abstract = True
        

def limit_owner_choices():
    adm_g = Group.objects.get(id='2')
    return {'is_staff': True, 'groups': adm_g} 
    
class MForm(Common): 
    owner = models.ForeignKey(User, verbose_name='Владелец', limit_choices_to=limit_owner_choices, help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы', related_name='own_mforms', null=True, blank=True)
    editor = models.ManyToManyField(User, verbose_name='Editors', limit_choices_to=limit_owner_choices, help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы', related_name='edit_mforms', null=True, blank=True)
    reader = models.ManyToManyField(User, verbose_name='Readers', limit_choices_to=limit_owner_choices, related_name='read_mforms', null=True, blank=True)
    mod_pass = models.PositiveSmallIntegerField('Модерация', choices=((0, ''), (1, 'на рассмотрении'), (2, 'одобрено'), (3, 'отклонено')), default='0')  
    comms = models.TextField('Комментарии', blank=True)    
    syn_form = models.ForeignKey(Form, verbose_name='Форма синхронизации', unique=True, null=True, blank=True, related_name='m_form')
    full_name = models.CharField('Название', max_length=250, unique=True)
    name = models.CharField('Краткое название', max_length=250, unique=True)
    info = models.TextField('Текстовая информация', blank=True)
    clarification = models.TextField('Пояснения', blank=True)
    theme = models.ForeignKey(Theme, verbose_name='Тема')
    class Meta:
        verbose_name = 'Форма для представления к модерации'
        verbose_name_plural = 'Формы для представления к модерации'

    def view_form(self):
        return format_html('<a href="' + reverse('lkmoderation:showform', args=(self.id,)) + '">Внешний вид</a>')
    view_form.short_description = 'Внешний вид'
        
    def delete_mform(self):
        if self.syn_form:
            if self.req.all()[0].passed == 0 and self.req.all()[0].type == 0:
                return self.get_mod_pass_display()
            elif self.req.all()[0].type == 0:
                return format_html('<b><i>' + self.get_mod_pass_display() + '</i></b><br>' + self.comms + '<br><a href="' + reverse('lkmoderation:askmod', args=(self.id, '0',)) + '">Ask moderation</a>')
            elif self.req.all()[0].passed == 0:
                return ''
            else:
                return format_html('<a href="' + reverse('lkmoderation:askmod', args=(self.id, '0')) + '">Ask moderation</a>')  
        else:
            return format_html('<a href="' + reverse('lkmoderation:sfdelete', args=(self.id,)) + '">Удалить</a>')
    delete_mform.short_description = 'Удалить'
    
    def show_rights(self):
        s = ''
        if self.owner:
            s = s + '<i>Owner:</i> ' + str(self.owner)
        if self.editor.all():
            s = s + '<br><i>Editors: </i>'
            for e in self.editor.all():
                s = s + str(e) + ', '
        if self.reader.all():
            s = s + '<br><i>Readers: </i>'
            for r in self.reader.all():
                s = s + str(r) + ', '
        return format_html(s)
    show_rights.short_description = 'Права'
    
    def show_syn_form(self):
        if self.syn_form:
            return format_html('<a href="/admin/lkforms/form/' + str(self.syn_form.id) + '">Перейти</a>')
        elif self.req.all():
            if self.mod_pass == 1:
                return self.get_mod_pass_display()
            else:
                return format_html('<b><i>' + self.get_mod_pass_display() + '</i></b><br>' + self.comms + '<br><a href="' + reverse('lkmoderation:askmod', args=(self.id, '1',)) + '">Ask moderation</a>')
        else:
            return format_html('<a href="' + reverse('lkmoderation:askmod', args=(self.id, '1', )) + '">Ask moderation</a>')
    show_syn_form.short_description = 'Форма синхронизации'

    def ask_moderation(self, type):
        if self.syn_form:
            if self.req.all()[0].passed == 0 and self.req.all()[0].type == int(type):
                return self.get_mod_pass_display()
            elif self.req.all()[0].type == int(type):
                return format_html('<b><i>' + self.get_mod_pass_display() + '</i></b><br>' + self.comms + '<br><a href="' + reverse('lkmoderation:askmod', args=(self.id, type, )) + '">Ask moderation</a>')
            elif self.req.all()[0].passed == 0:
                return ''
            else:
                return format_html('<a href="' + reverse('lkmoderation:askmod', args=(self.id, type)) + '">Ask moderation</a>')  
        else:
            return ''
            
    def syn_questions(self):
        return self.ask_moderation('2')
    syn_questions.short_description = 'Синхронизировать'

    def reg_to_arch(self):
        return self.ask_moderation('3')
    reg_to_arch.short_description = 'Архивировать регистрации'   

    def res_to_arch(self):
        return self.ask_moderation('4')
    res_to_arch.short_description = 'Архивировать результаты'     
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name 

        
class MQuestion(Common):
    owner = models.ForeignKey(User, verbose_name='Владелец', limit_choices_to=limit_owner_choices, help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы', related_name='own_mqns', null=True, blank=True)
    name = models.CharField('Вопрос', max_length=250)
    comms = models.TextField('Пояснения', blank=True, default='')
    not_blank = models.BooleanField('Обязательный', default=False)
    with_vars = models.BooleanField('С вариантами ответа', default=False)
    multi_vars = models.BooleanField('Несколько вариантов ответа', default=False)
    class Meta:
        verbose_name = 'Вопрос для представления к модерации'
        verbose_name_plural = 'Вопросы для представления к модерации'
        ordering = ['name']
        
    def delete_mqn(self):
        return format_html('<a href="' + reverse('lkmoderation:sqdelete', args=(self.id,)) + '">Удалить</a>')
    delete_mqn.short_description = 'Удалить'
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
        


class MVariant(Common):
    question = models.ForeignKey(MQuestion, related_name='variant_list')
    name = models.CharField('Вариант', max_length=250)
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
        
        
class MFmQn(Common):
    form = models.ForeignKey(MForm, verbose_name='Форма для представления к модерации', related_name='mfmqn_fmlist')
    question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='mfmqn_qnlist')
    number = models.CharField('Номер вопроса', max_length=3, blank=True, default='')
    class Meta:
        verbose_name = 'Одобренный вопрос'
        verbose_name_plural = 'Одобренные вопросы'

    def __str__(self):
        return self.question.name
    def __unicode__(self):
        return self.question.name
        

class MFmMQn(Common):
    form = models.ForeignKey(MForm, verbose_name='Форма для представления к модерации', related_name='mfmmqn_fmlist')
    question = models.ForeignKey(MQuestion, verbose_name='Вопрос', related_name='mfmmqn_qnlist')
    number = models.CharField('Номер вопроса', max_length=3, blank=True, default='')
    class Meta:
        verbose_name = 'Неодобренный вопрос'
        verbose_name_plural = 'Неодобренные вопросы'

    def __str__(self):
        return self.question.name
    def __unicode__(self):
        return self.question.name
        
              
class Request(Common):
    form = models.ForeignKey(MForm, unique=True, verbose_name='Форма для представления к модерации', related_name='req')
    author = models.ForeignKey(User, verbose_name='Автор запроса', related_name='req_list')
    type = models.PositiveSmallIntegerField('Тип запроса', choices=((0, 'удалить'), (1, 'создать'), (2, 'синхронизировать'),(3, 'регистрации в архив'),
                                                                    (4, 'результаты в архив')), default='0') 
    moderator = models.ForeignKey(User, verbose_name='Модератор', null=True, blank=True, related_name='mod_list')
    passed = models.PositiveSmallIntegerField('Модерация', choices=((0, ''), (1, 'одобрено'), (2, 'отклонено')), default='0') 
    class Meta:
        verbose_name = 'Запрос на модерацию формы'
        verbose_name_plural = 'Запросы на модерацию формы'

    def __str__(self):
        return self.form.name
    def __unicode__(self):
        return self.form.name
        
              
class QRequest(Common):
    question = models.ForeignKey(Question, unique=True, verbose_name='Вопрос для представления к модерации', related_name='qreq')
    author = models.ForeignKey(User, verbose_name='Автор запроса', related_name='qreq_list')
    type = models.PositiveSmallIntegerField('Тип запроса', choices=((0, 'удалить'), (1, 'архивировать')), default='0') 
    moderator = models.ForeignKey(User, verbose_name='Модератор', null=True, blank=True, related_name='qmod_list')
    passed = models.PositiveSmallIntegerField('Модерация', choices=((0, ''), (1, 'одобрено'), (2, 'отклонено')), default='0') 
    comms = models.TextField('Комментарии', blank=True) 
    class Meta:
        verbose_name = 'Запрос на модерацию вопроса'
        verbose_name_plural = 'Запросы на модерацию вопроса'

    def __str__(self):
        return self.question.name
    def __unicode__(self):
        return self.question.name
