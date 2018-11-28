import django_tables2 as tables
# noinspection PyUnresolvedReferences
from start_page import models


class SubjectTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')
    delete = tables.TemplateColumn(verbose_name='Usuń',
                                   template_name='object_delete/button_delete_template.html',
                                   extra_context={
                                       'edit_button': True,
                                   })

    class Meta:
        model = models.Subject
        fields = ['name', 'short_name']
