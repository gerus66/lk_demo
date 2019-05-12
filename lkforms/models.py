from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
import csv
from django.core.urlresolvers import reverse
from django.db.models import Q

MAIL_TEMPLATE_ID = 112

#metaclass
class Common(models.Model):
    created = models.DateTimeField('создан', auto_now_add=True)
    changed = models.DateTimeField('изменен', auto_now=True)
    class Meta:
        abstract = True

#User - базовый профиль (email, username, activated)
#UserProfile - расширенный профиль, к которому все привязано
class UserProfile(Common):
    user = models.ForeignKey(User, unique=True, verbose_name='Логин', related_name='profile')
    sname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    pname = models.CharField('Отчество', max_length=50)
    sex = models.PositiveSmallIntegerField('Пол', choices=((0, 'выбрать'), (1, 'жен'), (2, 'муж')), default='0')
    bday = models.DateField('Дата рождения')
    src = models.PositiveSmallIntegerField('Источник', choices=((0, 'выбрать'),(1, 'интернет'),(2, 'учитель'),(3, 'знакомый'),
                                            (4, 'email письмо'),(5, 'журнал "Квант"'),(6, 'журнал "Потенциал"'),(7, 'ВЗМШ'),(8, 'другое')), default='0')
    yasrc = models.CharField('Другое', max_length=500, blank=True)
    year = models.IntegerField('Год выпуска', default='0', help_text = '1900 - для взрослых, 2100 - для маленьких')
    diploms = models.TextField('Дипломы', blank = True, default = '')
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    #quick link to User 
    def show_email(self):
        return format_html("<a href='/admin/auth/user/{}'>{}</a>", self.user.id, self.user.email)
    show_email.short_description = 'Основной профиль'
    show_email.admin_order_field = 'user.email'
    
    #quick links 'mailto:' and to some template
    def send_email(self):
        return format_html("<a href='mailto:{}'>mail to..</a><br/><a href='/lk/formsuserprofile/delete_email/{}/'>mail template</a><a href='/admin/lkforms/external/{}/'>(this one)</a>", 
                            self.user.email, self.user.id, MAIL_TEMPLATE_ID)
    send_email.short_description = 'Послать письмо'

    def make_profile(self):
        buf = [['login', self.user.username.encode('utf8')], ['e-mail', self.user.email.encode('utf8')], 
		        ['name', self.sname.encode('utf8') + ' ' + self.name.encode('utf8') + ' ' + self.pname.encode('utf8')], ['birthday', self.bday],
                ['sex', self.get_sex_display().encode('utf8')], ['src', self.get_src_display().encode('utf8') + ' ' + self.yasrc.encode('utf8')],
                ['created', self.created], ['registrations and results'],
                ['form', 'registration', 'result', 'detail result', 'private result', 'created', 'last change']]
        for f in Form.objects.all():
            s = ['', '', '', '', '', '', '']
            if RegRes.objects.filter(user=self).filter(form=f):
                rr = RegRes.objects.filter(user=self).filter(form=f)[0]
                s = [f.name.encode('utf8'), '', '', rr.detail_result.encode('utf8'), rr.private_result.encode('utf8'), rr.created, rr.changed]
                if rr.is_checkin:
                    s[1] = 'yes'
                if rr.short_result != 0:
                    s[2] = rr.get_short_result_display().encode('utf8')
            if ArchiveRegRes.objects.filter(user=self).filter(form=f):
                arr = ArchiveRegRes.objects.filter(user=self).filter(form=f)[0]
                s[0] = f.name.encode('utf8')
                if arr.is_checkin:
                    s[1] = s[1] + '(a) yes'
                if arr.short_result != 0:
                    s[2] = s[2] + '(a) ' + arr.get_short_result_display().encode('utf8')
                if arr.detail_result != '':
                    s[3] = s[3] + '(a) ' + arr.detail_result.encode('utf8')
                if arr.private_result != '':
                    s[4] = s[4] + '(a) ' + arr.private_result.encode('utf8')
            if s != ['', '', '', '', '', '', '']:
                buf.append(s)
        buf = buf + [['questions'], ['question', 'answer', 'created', 'last change']]
        for a in self.answer_profile.all():
            buf.append([a.question.name.encode('utf8'), a.answer.encode('utf8'), a.created, a.changed])
        for aa in self.archanswer_profile.all():
            buf.append([aa.question_text.encode('utf8'), '(a) ' + aa.answer.encode('utf8')])
        f = open('/var/www/lk/media/profiles/' + str(self.id) + '_all.csv', 'wb')
        wrtr = csv.writer(f, delimiter=';')
        for b in buf:
            wrtr.writerow(b)
        return 1

    def download_profile(self):
        return format_html('<a href="/admin/download/profiles/' + str(self.id) + '_all.csv">' + str(self.id) + '_all.csv</a>')
    download_profile.short_description = 'Скачать данные о пользователе'

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username



class Question(Common):
    name = models.CharField('Вопрос', max_length=250)
    comms = models.TextField('Пояснения', blank=True, default='')
    eng = models.TextField('English version', blank = True, default = '')
    not_blank = models.BooleanField('Обязательный', default=False)
    with_vars = models.BooleanField('С вариантами ответа', default=False)
    multi_vars = models.BooleanField('Несколько вариантов ответа', default=False)
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['name']

    def used_by_forms(self):
        list = ''
        for fq in self.fmqn_qnlist.all():
            list = list + '<a href="/admin/lkforms/form/' + str(fq.form.id) + '">' + str(fq.form.id) + '</a>, '
        return format_html(list)
    used_by_forms.short_description = 'Привязан к формам'

 #   def last_archivation(self):
 #       if self.archanswer_list.count():
 #           return self.archanswer_list.all().order_by('-changed')[0].changed
 #       else:
 #           return ''
 #   last_archivation.short_description = 'Архивирован (последний раз)'
    
    def counts(self):
        return self.answer_list.count()
    counts.short_description = 'Количество ответов'
        
    def make_archive(self):
        return format_html('<a href="' + reverse('lkforms:qn_to_archive', args=(self.id,)) + '">В архив</a>')
    make_archive.short_description = 'Архивировать'

    def ask_moderation(self, type):
        if self.qreq.all():
            if self.qreq.all()[0].passed == 0 and self.qreq.all()[0].type == int(type):
                return 'на рассмотрении'
            elif self.qreq.all()[0].type == int(type):
                return format_html('<b><i>' + self.qreq.all()[0].get_passed_display() + '</i></b><br>' + self.qreq.all()[0].comms + '<br><a href="' + reverse('lkmoderation:askmod', args=(self.id, '1' + type)) + '">Ask moderation</a>')
            elif self.qreq.all()[0].passed == 0:
                return ''
        return format_html('<a href="' + reverse('lkmoderation:askmod', args=(self.id, '1' + type)) + '">Ask moderation</a>')  
        
    def ask_archive(self):
        return self.ask_moderation('1')
    ask_archive.short_description = 'Архивировать'
        
    def delete_qn(self):
        return self.ask_moderation('0')
    delete_qn.short_description = 'Удалить'
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Variant(Common):
    question = models.ForeignKey(Question, related_name='variant_list')
    name = models.CharField('Вариант', max_length=250)
    eng = models.CharField('English version', max_length = 250, blank = True, default = '')
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

def result_path(self, result):
    return ("result/" + str(self.id) + "_res.csv")
    
def default_list_path(self, default_list):
    return ("default/" + str(self.id) + "_def.csv")
    
def test_answers_path(self, test_answers):
    return ("answers/" + str(self.id) + "_ans.csv")

def limit_owner_choices():
    adm_g = Group.objects.get(id='2')
    return {'is_staff': True, 'groups': adm_g}   
    
def limit_reader_choices():
    read_g = Group.objects.get(id='3')
  #  adm_g = Group.objects.get(id='2')
    return {'is_staff': True, 'groups': read_g }
  # return Q('is_staff'=True)# & ( Q(Group.objects.get(id='2')) | Q(Group.objects.get(id='3'))  


class Theme(Common):
    name = models.CharField('Тема', max_length=250, unique=True)
    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
        
    
class Form(Common):      
    full_name = models.CharField('Название', max_length=250)
    full_name_eng = models.CharField('English version of full_name', max_length=250, blank = True, default = '')
    name = models.CharField('Краткое название', max_length=250, unique=True)
    name_eng = models.CharField('English version of name', max_length=250, blank = True, default = '')
    theme = models.ForeignKey(Theme, verbose_name='Тема', related_name='form_list')
    user_theme = models.ForeignKey(Theme, verbose_name='Тема для отображения у пользователя', related_name='form_userlist')
    not_reversed = models.BooleanField('Невозвратная', default=False)
    is_active = models.BooleanField('Активна', default=False)
    help_info = models.TextField('Скрытая памятка', blank=True, help_text='Доступна владельцу и редактору формы')
    info = models.TextField('Текстовая информация', blank=True, help_text='Отображается в конце формы перед снопкой Сохранить')
    info_eng = models.TextField('English version of info', blank = True, default = '')
    clarification = models.TextField('Пояснения', blank=True, help_text='Отображается в начале формы перед всеми вопросами и в таблице активных форм в отдельной графе')
    clarification_eng = models.TextField('English version of clarification', blank = True, default = '')
    start_time = models.DateTimeField('Время начала', blank=True, null=True, help_text='Для корректной работы должно быть указано и время начала, и время окончания. <br>Значение поля "Активна" не имеет значения.')
    finish_time = models.DateTimeField('Время окончания', blank=True, null=True, help_text='Для корректной работы должно быть указано и время начала, и время окончания. <br>Значение поля "Активна" не имеет значения.')
    aif = models.ManyToManyField('self', verbose_name='avaliable for user registered to (OR)', blank=True, symmetrical=False, related_name='aif_set')
    unaif = models.ManyToManyField('self', verbose_name='unavaliable for user registered to (OR)', blank=True, symmetrical=False, related_name='unaif_set')
    aifpass = models.ManyToManyField('self', verbose_name='avaliable for users passed (OR)', blank=True, symmetrical=False, related_name='aifpass_set')
    aifres = models.ManyToManyField('self', verbose_name='avaliable for users in reserve for (OR)', blank=True, symmetrical=False, related_name='aifres_set')
    file = models.FileField('Прикрепленный файл', help_text='Название файла не должно содержать русских букв.<br>Если Вы создаете новый объект, сохраните его(Сохранить и продолжить редактирование), прежде чем прикреплять к нему файл.', upload_to='for_users', blank=True)
    result = models.FileField('Результаты', help_text='Файл формата .csv, <b>кодировка Windows-1251 (стандартный Excel)</b>. Колонки: <br>(1)Фамилия, (2)Имя, (3)Отчество, (4)Дата рождения - обязательно заполненные, название любое.<br>(5)Зачет, (6)Резерв, (7)Незачет - <br> - отмечаются словом <b>yes</b> (учитывается первое встреченное), изменяя "краткий результат" на соответствующий;<br> - в случае, если ни одна не отмечена (или отмечены неверно), за "кратким результатом" сохраняется статус "неопределен";<br> - название отмеченной колонки записывается в "детальный результат" и доступно для просмотра школьнику. <br>(7), ...<br> - по умолчанию записывается в "детальный результат" (и доступно для просмотра школьнику) в виде <i>название колонки</i>: <i>значение для данного школьника</i><br> - в случае префикса Priv в названии колонки записывается в "скрытый результат" и не доступно для просмотра школьнику;<br> - может содержать ссылки на автоматически формирующийся pdf-файл - по отдельной договоренности с разработчиком.<br>Если Вы создаете новый объект, сохраните его(Сохранить и продолжить редактирование), прежде чем прикреплять к нему файл.', upload_to=result_path, blank=True)
    default_list = models.FileField('Эталонный список', help_text='Файл формата .csv с обязательными колонками Ф/И/О/Д.р. Последующие столбцы игнорируются. В случае неполных данных по человеку(ФИ обязательны!), производится выборка подходящих вариантов из числа зарегистрированных на данную форму. <br><b>Кодировка файла Windows-1251 (стандартный Excel)</b><br>Если Вы создаете новый объект, сохраните его(Сохранить и продолжить редактирование), прежде чем прикреплять к нему файл.', upload_to=default_list_path, blank=True)
    test_answers = models.FileField('Ответы для автоматической проверки', help_text='Файл формата .csv с 4 пустыми колонками, далее в 1й строке вопросы вида "id.любой текст", во 2й-4й строках ответы на них, в 5й - стоимость правильного ответа. Пустыми ячейки ответов оставлять нельзя, дублировать можно.<br>В ответах: <br> - регистр не имеет значения<br> - запятые равны точкам<br> - е равно ё<br> - начальные и конечные пробелы игнорируются<br> - 1й символ _ означает, что пробелы и ; игнорируются<br> - 1й или 2й символ * означает, что игнорируется весь текст до первой цифры или минуса<br> - символы # или $ в конце ответа означают, что после может идти любой текст ( в случае $ не начинающийся с цифры или точки)<br><b>Кодировка файла UTF-8 (Юникод)</b><br>Если Вы создаете новый объект, сохраните его(Сохранить и продолжить редактирование), прежде чем прикреплять к нему файл.', upload_to=test_answers_path, blank=True)
    last_reg_archivation = models.DateField('Архивация регистраций (последняя)', null=True)
    last_res_archivation = models.DateField('Архивация результатов (последняя)', null=True)
    last_res_publication = models.DateField('Публикация результатов (последняя)', null = True)
    owner = models.ForeignKey(User, verbose_name='Владелец', limit_choices_to=limit_owner_choices, help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы', related_name='own_forms', null=True, blank=True)
    editor = models.ManyToManyField(User, verbose_name='Editors', limit_choices_to=limit_owner_choices, help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы', related_name='edit_forms', null=True, blank=True)
    reader = models.ManyToManyField(User, verbose_name='Readers', help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы или Читатели', limit_choices_to=limit_reader_choices, related_name='read_forms', null=True, blank=True)
    just_user = models.ManyToManyField(User, verbose_name='Just users', related_name='use_forms', null=True, blank=True)
    class Meta:
        verbose_name = 'Форма с вопросами'
        verbose_name_plural = 'Формы с вопросами'
    
    def show_rights(self):          
        s = ''
        if self.owner:
            s = ' '.join([s, '<i>Owner:</i>', self.owner.profile.all()[0].sname, self.owner.profile.all()[0].name, self.owner.profile.all()[0].pname])
        if self.editor.all():
            s = ' '.join([s, '<br><i>Editors:</i>', ', '.join([' '.join([e.profile.all()[0].sname, e.profile.all()[0].name, e.profile.all()[0].pname]) for e in self.editor.all()])])
        if self.reader.all():
            s = ' '.join([s, '<br><i>Readers:</i>', ', '.join([' '.join([r.profile.all()[0].sname, r.profile.all()[0].name, r.profile.all()[0].pname]) for r in self.reader.all()])])
        if self.just_user.all():
            s = ' '.join([s, '<br><i>Just users:</i>', ', '.join([' '.join([u.profile.all()[0].sname, u.profile.all()[0].name, u.profile.all()[0].pname]) for u in self.just_user.all()])])
        return format_html(s)
    show_rights.short_description = 'Права'
    
    def show_owner(self):
        if self.owner:
            return ' '.join([self.owner.profile.all()[0].sname, self.owner.profile.all()[0].name, self.owner.profile.all()[0].pname])
        return ''
    show_owner.short_description = "Владелец"
    
    def view_form(self):
        return format_html(''.join(['<a href="' + reverse('lkforms:showform', args=(self.id,)) + '">Посмотреть</a>']))
    view_form.short_description = 'Внешний вид'

    def show_syn_form(self):
        if self.m_form.all():
            return format_html('<a href="/admin/lkmoderation/mform/' + str(self.m_form.all()[0].id) + '">Перейти</a>')
        elif self.owner:
            return format_html('<a href="' + reverse('lkmoderation:new_syn_mform', args=(self.id,)) + '">Создать</a>')
        else:
            return format_html('<span class="small quiet">сначала назначьте владельца формы</span>')
    show_syn_form.short_description = 'Модерация'
    
    
    def registration_count(self):
        return len([ rr for rr in self.regres_list.all() if rr.is_checkin ])
    registration_count.short_description = 'Регистраций'

    #def archivation_show(self):
    #    return format_html('<i>регистраций:</i><br>' + str(self.last_reg_archivation) + '<br><i>результатов:</i><br>' + str(self.last_res_archivation))
    #archivation_show.short_description = 'Архивация (посл.)'
    
    def make_archive(self):
        return format_html('</br>'.join(['<a href="{0}">Registrations</a>', 'last: {2}', '<a href="{1}">Results</a>', 'last: {3}']).format(
            reverse('lkforms:reg_to_archive', args=(self.id,)), reverse('lkforms:res_to_archive', args=(self.id,)), self.last_reg_archivation, self.last_res_publication
        ))
    make_archive.short_description = 'Архивировать'
    
    def make_txt(self):
        txt = []
        txt.append(str(self.id) + '. ' + self.name.encode('utf8'))
        txt.append('\n' + self.full_name.encode('utf8'))
        for fq in self.fmqn_fmlist.order_by('number'):
            s = ''
            if fq.is_priv:
                s = s + 'priv '
            if fq.question.not_blank:
                s = s + '*'
            s = '\n\n' + s + fq.number.encode('utf8') + '. ' + fq.question.name.encode('utf8')
            txt.append(s)
            if fq.question.comms != '':
                txt.append('\n' + str(fq.question.comms.encode('utf8')))
            if fq.question.with_vars:
                for v in fq.question.variant_list.order_by('name'):
                    txt.append('\n- ' + v.name.encode('utf8'))
        txt.append('\n\n' + self.info.encode('utf8'))
        f = open('/var/www/lk/media/txt/' + str(self.id) + '.txt', 'wb')
        f.writelines(txt)
        return 1

    def download_txt(self):
        s = ''.join(['<a href="/admin/download/txt/', str(self.id), '.txt">', str(self.id), '.txt</a>'])
        if self.id == 163:   # for MM overall csv
            s = ''.join([s, '<br><a href="/lk/formsform/generate_mm/">refresh</a><br><a href="/admin/download/data/mm.csv">mm.csv</a>'])
        return format_html(s)
    download_txt.short_description = 'Скачать'   
    download_txt.admin_order_field = 'id'

    def user_download_txt(self):
        return format_html('<a href="/lk/forms/download/txt/' + str(self.id) + '.txt">' + str(self.id) + '.txt</a>')
    user_download_txt.short_description = 'Скачать'
    
    def set_result(self):
        if self.last_res_publication:
            s = 'last: {0:%d}-{0:%m}-{0:%Y}'.format(self.last_res_publication)
        else:
            s = 'last:'
        if self.result:
            s = '</br>'.join(['<a href="/admin/download/{0}">Publication</a>', s,
                              '<a href="/admin/download/diploms_{0}">Diploms</a>',
                              '<a href="/admin/download/read_{0}">Show recent file</a>']).format(self.result.name)
        return format_html(s)  
    set_result.short_description = 'Результаты'

    def check_test(self):
        if self.test_answers:
            return format_html('<a href="/admin/download/' + self.test_answers.name + '">Check</a><br><a href="/admin/download/read_' + self.test_answers.name + '">Show recent file</a>')
        return ''
    check_test.short_description = 'Автопроверка'
    
    def compare_lists(self):
        if self.default_list:
            return format_html('<a href="/admin/download/' + self.default_list.name + '">Compare</a><br><a href="/admin/download/read_' + self.default_list.name + '">Show recent file</a>')
        return ''
    compare_lists.short_description = 'Списки'
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class FmQn(Common):
    form = models.ForeignKey(Form, verbose_name='Форма с вопросами', related_name='fmqn_fmlist')
    question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='fmqn_qnlist')
    number = models.CharField('Номер вопроса', max_length=3, blank=True, default='')
    is_priv = models.BooleanField('Скрытый', default=False)
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question.name
    def __unicode__(self):
        return self.question.name


class Answer(Common):
    user = models.ForeignKey(UserProfile, verbose_name='Логин', related_name='answer_profile')
    question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='answer_list')
    answer = models.CharField('Ответ', max_length=500, blank=True, default='')
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.question.name
    def __unicode__(self):
        return self.question.name

		
class RegRes(Common):
    user = models.ForeignKey(UserProfile, verbose_name='Логин', related_name='regres_profile')
    form = models.ForeignKey(Form, verbose_name='Форма', related_name='regres_list')
    is_checkin = models.BooleanField('Регистрация пройдена', default=False)
    short_result = models.PositiveSmallIntegerField('Результат', choices=((0, 'неопределен'),(1, 'зачет'),(2, 'незачет'),(3, 'в  резерве')), default=0)
    detail_result = models.TextField('Детальный результат', blank=True, default='')
    private_result = models.TextField('Скрытый результат', blank=True, default='')
    class Meta:
        verbose_name = 'Регистрации и результаты'
        verbose_name_plural = 'Регистрации и результаты'

    def __str__(self):
        return self.form.name
    def __unicode__(self):
        return self.form.name


class ArchiveAnswer(Common):
    user = models.ForeignKey(UserProfile, verbose_name='Логин', related_name='archanswer_profile')
 #   question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='archanswer_list')
    question_text = models.CharField('Вопрос', max_length=500, blank=True, default='')
    answer = models.CharField('Ответ', max_length=500, blank=True, default='')
    class Meta:
        verbose_name = 'Ответы (архив)'
        verbose_name_plural = 'Ответы (архивы)'

    def __str__(self):
        return self.question_text
    def __unicode__(self):
        return self.question_text


class ArchiveRegRes(Common):
    user = models.ForeignKey(UserProfile, verbose_name='Логин', related_name='archregres_profile')
    form_name = models.CharField('Форма', max_length=250, blank=True, default='')
    form = models.ForeignKey(Form, verbose_name='Форма', related_name='archregres_list')
    is_checkin = models.BooleanField('Регистрация пройдена', default=False)
    short_result = models.PositiveSmallIntegerField('Результат', choices=((0, 'неопределен'),(1, 'зачет'),(2, 'незачет'),(3, 'в резерве')), default=0)
    detail_result = models.TextField('Детальный результат', blank=True, default='')
    private_result = models.TextField('Скрытый результат', blank=True, default='')
    class Meta:
        verbose_name = 'Регистрации и результаты (архив)'
        verbose_name_plural = 'Регистрации и результаты (архив)'

    def __str__(self):
        return self.form.name
    def __unicode__(self):
        return self.form.name

def exfile_path(self, exfile):
    return ("external/" + str(self.id) + "_ext.csv")
        
class External(Common):   
    exfile = models.FileField('Файл', help_text='Файл формата .csv с обязательными колонками: Ф/И/О/Д.р. <br>Для <b>загрузки ответов</b> последующие колонки должны иметь заголовок id_вопроса.[любой текст] <br>Для <b>поиска профилей</b> колонки Д.р. и Отчество могут быть пустыми, но в этом случае остальные опции недоступны<br><b>Кодировка файла Windows-1251 (стандартный Excel)</b>', upload_to=exfile_path, blank=True)
    is_utf = models.BooleanField('UTF-8', default=False)
    original = models.CharField('Пояснения', max_length=250)
    letter = models.TextField('Текст письма', blank=True, default='')
    letter_abs = models.CharField('Тема письма', max_length=200, blank=True, default='')
    owner = models.ForeignKey(User, verbose_name='Владелец', limit_choices_to=limit_owner_choices, related_name='own_external', help_text='В списке выбора только пользователи, обладающие статусом персонала и состоящие в группе Администраторы')
    class Meta:
        verbose_name = 'Внешние данные'
        verbose_name_plural = 'Внешние данные'
        
    def set(self):
        if self.exfile:
            return format_html('<a href="/admin/download/set_' + self.exfile.name + '">Download data</a><br><span class="help">File saved ' + self.changed.strftime("%Y-%m-%d %H:%M:%S") + '</span>')
        return ''
    set.short_description = 'Загрузить данные'
        
    def send(self):
        if self.letter and self.letter_abs and self.exfile:
            return format_html('<a href="/admin/download/send_' + self.exfile.name + '">Send mail</a><br><span class="help">File saved ' + self.changed.strftime("%Y-%m-%d %H:%M:%S") + '</span>')
        if self.letter and self.letter_abs:
            return format_html('<a href="/admin/download/send_all/' + str(self.id) + '_all.csv">Send to all</a>')
        return ''
    send.short_description = 'Отправить письма'        
        
    def find(self):
        if self.exfile:
            return format_html('<a href="/admin/download/find_' + self.exfile.name + '">Find profiles</a><br><span class="help">File saved ' + self.changed.strftime("%Y-%m-%d %H:%M:%S") + '</span>')
        return ''
    find.short_description = 'Найти профили' 
        
    def get(self):
        if self.exfile:
            return format_html('<a href="/admin/download/read_' + self.exfile.name + '">Show recent file</a>')
        return ''
    get.short_description = 'Просмотреть файл'    
        
    def show_owner(self):
        return ' '.join([self.owner.profile.all()[0].sname, self.owner.profile.all()[0].name, self.owner.profile.all()[0].pname])
    show_owner.short_description = 'Владелец'
    show_owner.admin_order_field = 'owner__id'
                
    def __str__(self):
        return self.original
    def __unicode__(self):
        return self.original

def list_person_path(self, list_person):
    return ("documents/" + str(self.id) + "_doc.csv")

class Doc(Common):   
    name = models.CharField('Название', max_length=250, unique=True)
    prefix = models.CharField('Уникальный префикс', max_length=10, unique=True)
    list_person = models.FileField('Файл', help_text='Файл формата .csv с обязательными колонками: Ф/И/О/Д.р. <br><b>Кодировка файла UTF-8</b><br>Если Вы создаете новый объект, сохраните его(Сохранить и продолжить редактирование), прежде чем прикреплять к нему файл.', upload_to=list_person_path, blank=True)
    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'
                
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name        
