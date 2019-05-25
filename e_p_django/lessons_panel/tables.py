import django_tables2 as tables
from django.utils.safestring import mark_safe

from e_p_django.classes_app.models import Class
from e_p_django.schedules.models import Schedule


class ClassTable(tables.Table):
    # id = tables.Column()
    name = tables.Column(verbose_name='Nazwa')
    select_class = tables.TemplateColumn(
        verbose_name='Wybierz',
        template_name='lessons_panel/button_select_class.html'
    )

    class Meta:
        model = Class
        fields = ['name']
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
