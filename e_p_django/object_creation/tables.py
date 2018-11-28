import django_tables2 as tables
# noinspection PyUnresolvedReferences
from start_page import models


class SubjectTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='object_delete/button_delete_template.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='object_edit/button_edit_template.html'
    )

    class Meta:
        model = models.Subject
        fields = ['name', 'short_name']
        attrs = {
            'class': 'table-condensed'
        }
