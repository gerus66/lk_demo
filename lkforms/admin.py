from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.utils import timezone
from lkforms.models import Common, UserProfile, Form, Question, Variant, FmQn, Answer, RegRes, ArchiveAnswer, ArchiveRegRes, External, Theme, Doc
from django.db.models import Q
from django.contrib.auth.models import Group

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
    list_display = ('id', 'name', 'not_blank', 'with_vars', 'used_by_forms', 'counts', 'make_archive')
    list_display_links = ('name',)
    fields = ('name', 'comms', 'not_blank', 'with_vars', 'multi_vars')
    search_fields = ['name',]
    save_as = True
    
    def get_queryset(self, req):
        qs = super(QuestionAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs
        else:
            ids = []
            for q in qs:
                for fq in q.fmqn_qnlist.all():
                    if fq.form.owner == req.user or req.user in fq.form.editor.all():
                        ids.append(fq.question.id)                
            return qs.filter(id__in=set(ids))
        
    def get_list_display(self, req):
        ld = super(QuestionAdmin, self).get_list_display(req)
        if req.user.is_superuser:
            return ld
        return ('name', 'not_blank', 'with_vars', 'used_by_forms', 'counts', 'ask_archive', 'delete_qn')               
        
    def get_readonly_fields(self, req, obj):
        fs = super(QuestionAdmin, self).get_readonly_fields(req, obj)
        if req.user.is_superuser:
            return fs
        return ('name',)
        

class FmQnInline(admin.TabularInline):
    model = FmQn
    extra = 0
    raw_id_fields = ("question",)


class FormAdmin(admin.ModelAdmin):
    inlines = [FmQnInline]
    list_display = ('name', 'full_name', 'view_form', 'is_active', 'not_reversed', 'registration_count', 'make_archive', 'download_txt', 'set_result', 'check_test', 'compare_lists', 'show_rights', 'show_syn_form')
    list_display_links = ('name',)
    filter_horizontal = ('aif', 'unaif', 'aifpass', 'aifres', 'editor', 'reader')
    fieldsets = [ ( None, { 'fields': [ 'name' ] } ), 
	             ( 'Info', { 'fields': [ 'full_name', 'theme', 'user_theme', 'help_info', 'clarification', 'info' ], 'classes': [ 'collapse' ] } ), ( None, { 'fields': [ 'not_reversed' ] } ), ( None, { 'fields': [ 'is_active' ] } ), ( None, { 'fields': [ 'start_time' ] } ), ( None, { 'fields': [ 'finish_time' ] } ), ( 'Access', { 'fields': [ 'aif', 'unaif', 'aifpass', 'aifres' ], 'classes': [ 'collapse' ] } ), ( 'Files', { 'fields': [ 'file', 'result', 'default_list', 'test_answers' ], 'classes': [ 'collapse' ] } ), ( 'Permission', { 'fields': [ 'owner', 'editor', 'reader' ], 'classes': [ 'collapse' ] } )]
    search_fields = ['name', 'full_name']
    save_as = True
    list_filter = ('theme__name', 'not_reversed', 'is_active', 'user_theme__name')
    actions = ['download_forms_1', 'download_forms_2', 'download_forms_3', 'download_forms_4', 'download_forms_5']
    
    def get_queryset(self, req):
        qs = super(FormAdmin, self).get_queryset(req)
        if req.user.is_superuser or Group.objects.get(id=4) in req.user.groups.all():
            return qs
        return qs.filter(Q(owner=req.user) | Q(id__in=set([f.id for f in req.user.edit_forms.all()])) | Q(id__in=set([f.id for f in req.user.read_forms.all()])))
        
    def get_readonly_fields(self, req, obj):
        fs = super(FormAdmin, self).get_readonly_fields(req, obj)
        if req.user.is_superuser:
            return fs
        return ('name', 'theme', 'user_theme', 'not_reversed', 'help_info', 'owner', 'reader', 'editor' )
        
    def get_list_display(self, req):
        ld = super(FormAdmin, self).get_list_display(req)
        if req.user.is_superuser:
            return ld
        elif Group.objects.get(id=2) in req.user.groups.all():
            return ('name', 'full_name', 'view_form', 'show_syn_form', 'is_active', 'registration_count', 'download_txt', 'set_result', 'compare_lists', 'show_rights')
        else:
            return ('name', 'full_name', 'view_form', 'is_active', 'registration_count', 'download_txt', 'compare_lists', 'show_rights')
        
    def make_forms(self, qset, uset, qns_in, archreg_in):
        s = ''
        for q in qset:
            s = s + str(q.id) + '_'
        if len(s) > 40:
            s = s[:40] + 'etc_forms.csv'
        else:
            s = s + 'forms.csv'
        buf = [['E-mail', 'Surname', 'Name', 'Pname', 'Birthday', 'Sex']]
        for q in qset:
            buf[0].append(str(q.id) + '. ' + q.name.encode('utf-8'))
        if qns_in:
            ids = set([])
            for q in qset:
                ids = ids | set([ fq.question.id for fq in q.fmqn_fmlist.all() ])
            for id in ids:
                buf[0].append(str(id) + '. ' + Question.objects.get(id=id).name.encode('utf-8'))
        for q in qset:
            buf[0].append('first ' + str(q.id) + '. ' + q.name.encode('utf-8')) 
            buf[0].append('last ' + str(q.id) + '. ' + q.name.encode('utf-8'))            
        for u in uset:
            ustr = [u.user.email.encode('utf-8'),
             u.sname.encode('utf-8'),
             u.name.encode('utf-8'),
             u.pname.encode('utf-8'),
             u.bday,
             u.get_sex_display().encode('utf-8')]
            for q in qset:
                if u.regres_profile.filter(form=q):
                    if u.regres_profile.filter(form=q)[0].short_result == 0:
                        res_out = ''
                    else: 
                        res_out = '(' + u.regres_profile.filter(form=q)[0].get_short_result_display().encode('utf-8') + ')'
                    if u.regres_profile.filter(form=q)[0].is_checkin:
                        ustr.append('yes' + res_out)
                    else:
                        ustr.append('' + res_out)
                elif archreg_in and u.archregres_profile.filter(form=q):
                    if u.archregres_profile.filter(form=q)[0].short_result == 0:
                        res_out = ''
                    else: 
                        res_out = '(' + u.archregres_profile.filter(form=q)[0].get_short_result_display().encode('utf-8') + ')'
                    if u.archregres_profile.filter(form=q)[0].is_checkin:
                        ustr.append('(a) yes' + res_out)
                    else:
                        ustr.append('' + res_out)
                else:
                    ustr.append('')
            fl = 1
            if qns_in:
                fl = 0
                for id in ids:
                    if u.answer_profile.filter(question=Question.objects.get(id=id)):
                        ustr.append(u.answer_profile.filter(question=Question.objects.get(id=id))[0].answer.encode('utf-8'))
                        fl = 1
                    else:
                        ustr.append('')
            for q in qset:
                if u.regres_profile.filter(form=q):
                    ustr.append(u.regres_profile.filter(form=q)[0].created)
                    ustr.append(u.regres_profile.filter(form=q)[0].changed)
                else:
                    ustr.append('')
                    ustr.append('')
            if fl or 'yes' in ustr or '(a) yes' in ustr:
                buf.append(ustr)
        f = open('/var/www/lk/media/data/' + s, 'wb')
        wrtr = csv.writer(f, delimiter=';')
        for b in buf:
            wrtr.writerow(b)
        return s
    make_forms.short_description = 'Сформировать файл данных по списку форм и пользователей'

    def or_user_set(self, qset):
        ids = set([])
        for q in qset:
            ids = ids | set([ rr.user.id for rr in q.regres_list.all() if rr.is_checkin ])
        return [ UserProfile.objects.get(id=id) for id in ids ]
    or_user_set.short_description = 'Список пользователей, зарегистрированных на одну из данных форм'

    def and_user_set(self, qset):
        ids = set([ rr.user.id for rr in qset[0].regres_list.all() if rr.is_checkin ])
        for q in qset:
            ids = ids & set([ rr.user.id for rr in q.regres_list.all() if rr.is_checkin ])
        return [ UserProfile.objects.get(id=id) for id in ids ]
    and_user_set.short_description = 'Список пользователей, зарегистрированных на все из данных форм'

    def active_archive_form_set(self, qset):
        ids = set([])
        for q in qset:
            ids = ids | set([ rr.form.id for rr in q.regres_profile.all() if rr.is_checkin ]) | set([ rr.form.id for rr in q.archregres_profile.all() if rr.is_checkin ])
        return [ Form.objects.get(id=id) for id in ids ]
    active_archive_form_set.short_description = 'Список регистраций данных пользователей, включая архив'

    def download_forms_1(self, req, qset):
        s = self.make_forms(qset, UserProfile.objects.all(), 1, 0)
        return HttpResponseRedirect('/admin/download/data/' + s)
    download_forms_1.short_description = 'Скачать данные выбранных форм (вне зависимости от регистраций на них)'

    def download_forms_2(self, req, qset):
        s = self.make_forms(qset, self.or_user_set(qset), 1, 0)
        return HttpResponseRedirect('/admin/download/data/' + s)
    download_forms_2.short_description = 'Скачать данные выбранных форм (для активно зарег-ных хотя бы на одну из них)'

    def download_forms_3(self, req, qset):
        s = self.make_forms(qset, self.and_user_set(qset), 1, 0)
        return HttpResponseRedirect('/admin/download/data/' + s)
    download_forms_3.short_description = 'Скачать данные выбранных форм (для активно зарег-ных на каждую из них)'

    def download_forms_4(self, req, qset):
        s = self.make_forms(self.active_archive_form_set(self.or_user_set(qset)), self.or_user_set(qset), 0, 1)
        return HttpResponseRedirect('/admin/download/data/' + s)
    download_forms_4.short_description = 'Скачать профили(ВСЕ регистрации и рез-ты) активно зарег-ных хотя бы на одну из выбранных форм'

    def download_forms_5(self, req, qset):
        s = self.make_forms(self.active_archive_form_set(self.and_user_set(qset)), self.and_user_set(qset), 0, 1)
        return HttpResponseRedirect('/admin/download/data/' + s)
    download_forms_5.short_description = 'Скачать профили(ВСЕ регистрации и рез-ты) активно зарег-ных на каждую из выбранных форм'


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0  
    fields = ["answer",]
    raw_id_fields = ["form",]
    

class RegResInline(admin.TabularInline):
    model = RegRes
    extra = 0
    raw_id_fields = ("form",)


class ArchiveAnswerInline(admin.TabularInline):
    model = ArchiveAnswer
    extra = 0
 #   raw_id_fields = ("question",)


class ArchiveRegResInline(admin.TabularInline):
    model = ArchiveRegRes
    extra = 0
    raw_id_fields = ("form",)


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, RegResInline, ArchiveAnswerInline, ArchiveRegResInline]
    list_display = ('user', 'sname', 'name', 'pname', 'sex', 'bday', 'show_email', 'send_email', 'download_profile')
    list_display_links = ('user',)
    list_filter = ('sex', 'src')
    raw_id_fields = ("user",)
    fieldsets = [(None, {'fields': ['user', 'year', 'diploms']}),
	             ('Общая информация', {'fields': ['sname', 'name', 'pname', 'sex', 'bday', 'src', 'yasrc'], 'classes': ['collapse']})]
    search_fields = ['sname', 'name', 'pname', 'user__username', 'user__email']
    
    
class ExternalAdmin(admin.ModelAdmin):
    list_display = ('original', 'set', 'send', 'find', 'get', 'show_owner')
    list_display_links = ('original',)
    fields = ('original', 'exfile', 'is_utf', 'letter_abs', 'letter', 'owner')   
    
    def get_queryset(self, req):
        qs = super(ExternalAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs
        return qs.filter(owner=req.user)
        
    def get_readonly_fields(self, req, obj):
        fs = super(ExternalAdmin, self).get_readonly_fields(req, obj)
        if req.user.is_superuser:
            return fs
        return ('owner',)
        
    def get_list_display(self, req):
        ld = super(ExternalAdmin, self).get_list_display(req)
        if req.user.is_superuser:
            return ld
        return ('original', 'set', 'find', 'send', 'get')
  
    
    
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name',)


class DocAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name', 'prefix', 'list_person')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(External, ExternalAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Doc, DocAdmin)
