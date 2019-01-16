import django_tables2 as tables

from classes_app.models import Class


class ClassTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')

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
