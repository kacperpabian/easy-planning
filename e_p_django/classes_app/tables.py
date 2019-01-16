import django_tables2 as tables

from .models import Class


class ClassTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')

    deatils = tables.TemplateColumn(
        verbose_name='Szczegóły',
        template_name='classes_templates/button_details_class.html'
    )

    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='classes_templates/button_delete_class.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='classes_templates/button_edit_class.html'
    )

    class Meta:
        model = Class
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
