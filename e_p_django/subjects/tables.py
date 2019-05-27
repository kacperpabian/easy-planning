import django_tables2 as tables

from .models import Subject


class SubjectTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='subjects/button_delete_subject.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='subjects/button_edit_subject.html'
    )

    class Meta:
        model = Subject
        per_page = 15
        fields = ['name', 'short_name']
        attrs = {
            'class': 'table-condensed align-middle',
            'style': 'border-radius: 5px; \
                    width: 100%; \
                    margin: 0px auto; \
                    float: none;',
            'td': {
                "align": "center"
            },
            'th': {
                "style": 'text-align:center'
            }
        }
