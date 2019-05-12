# -*- coding: utf-8 -*-

from django.contrib import admin
from lkmoderation.models import MFmQn, MFmMQn, MForm, Request, MQuestion, QRequest, MVariant
from django.db.models import Q


class MFmQnInline(admin.TabularInline):
    model = MFmQn
    extra = 1


class MFmMQnInline(admin.TabularInline):
    model = MFmMQn
    extra = 1
    

class MFormAdmin(admin.ModelAdmin):
    inlines = [MFmQnInline, MFmMQnInline]
    list_display = ('name', 'full_name', 'clarification', 'view_form', 'owner', 'mod_pass')
    list_display_links = ('name',)
    fields = ('name', 'full_name', 'theme', 'clarification', 'info', 'owner', 'editor', 'reader', 'mod_pass', 'comms', 'syn_form')
    filter_horizontal = ('editor', 'reader')
    actions = None
    
    def get_queryset(self, req):
        qs = super(MFormAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs
        return qs.filter(Q(owner=req.user) | Q(syn_form__in=set(req.user.edit_forms.all())))
        
    def get_list_display(self, req):
        ld = super(MFormAdmin, self).get_list_display(req)
        if req.user.is_superuser:
            return ld
        return ('name', 'view_form', 'show_syn_form', 'syn_questions', 'reg_to_arch', 'res_to_arch', 'show_rights', 'delete_mform')
        
    def get_fields(self, req, obj):
        fs = super(MFormAdmin, self).get_fields(req, obj)
        if req.user.is_superuser:
            return fs
        if req.user == obj.owner:
            return ('name', 'full_name', 'theme', 'clarification', 'info', 'editor', 'reader')
        return ('name', 'full_name', 'theme', 'info', 'clarification')
        
    def get_readonly_fields(self, req, obj):
        fs = super(MFormAdmin, self).get_readonly_fields(req, obj)
        if obj:
            if not req.user.is_superuser and obj.syn_form:
                return ('name', 'full_name', 'theme', 'info', 'clarification')
        return fs


class MVariantInline(admin.TabularInline):
    model = MVariant
    extra = 1
    
    
class MQuestionAdmin(admin.ModelAdmin):
    inlines = [MVariantInline]
    list_display = ('name', 'not_blank', 'owner')
    list_display_links = ('name',)
    list_editable = ('not_blank',)
    fields = ('name', 'comms', 'not_blank', 'with_vars', 'multi_vars', 'owner')
   
    def get_queryset(self, req):
        qs = super(MQuestionAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs
        return qs.filter(owner=req.user)
        
    def get_list_display(self, req):
        ld = super(MQuestionAdmin, self).get_list_display(req)
        if req.user.is_superuser:
            return ld
        return ('name', 'not_blank', 'owner', 'delete_mqn')        
            
    def get_readonly_fields(self, req, obj):
        fs = super(MQuestionAdmin, self).get_readonly_fields(req, obj)
        if obj:
            if not req.user.is_superuser:
                return ('owner', )
        return fs
        
    
class RequestAdmin(admin.ModelAdmin):
    list_display = ('form', 'author', 'type', 'moderator', 'passed', 'changed') 
    list_display_links = ('form', )
    fields = ('form', 'author', 'type', 'moderator', 'passed') 
 #   date_hierarchy = 'changed'


class QRequestAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'type', 'moderator', 'passed', 'comms', 'changed') 
    list_display_links = ('question', )
    fields = ('question', 'author', 'type', 'moderator', 'passed', 'comms') 
 #   date_hierarchy = 'changed'
    
    
admin.site.register(MForm, MFormAdmin)
admin.site.register(MQuestion, MQuestionAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(QRequest, QRequestAdmin)
admin.site.disable_action('delete_selected')
