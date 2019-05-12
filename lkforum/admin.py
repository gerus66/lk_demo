# -*- coding: utf-8 -*-

from django.contrib import admin
from lkforum.models import QnAns, Receiver, Topic

class QnAnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'question', 'answer', 'is_private', 'show_author', 'show_receiver', 'created','changed')
    list_display_links = ('question', )
    fields = ('question', 'answer', 'is_private', 'topic', 'author', 'receiver')
    list_filter = ('topic__name', 'receiver__post')
#    date_hierarchy = 'created'
    actions = ['send_email', 'ya_send_email', 'delete_selected']
            
    def send_email(self, req, qset):
        for q in qset:
            q.make_receiver_email()
    send_email.short_description = 'Отправить письма адресатам данных вопросов'
            
    def ya_send_email(self, req, qset):
        for q in qset:
            q.make_author_email()
    ya_send_email.short_description = 'Отправить письма авторам данных вопросов'
    
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'extra_email')
    list_display_links = ('user', )
    fields = ('user', 'post', 'extra_email')
    
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'info', 'default_receiver')
    list_display_links = ('name',)
    fields = ('name', 'number', 'info', 'default_receiver')


admin.site.register(QnAns, QnAnsAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Topic, TopicAdmin)
