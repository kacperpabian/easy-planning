import django_tables2 as tables
# noinspection PyUnresolvedReferences
from .models import Schedule


class ScheduleTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa planu')
    description = tables.Column(verbose_name='Opis')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='schedules/button_delete_schedule.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='schedules/button_edit_schedule.html'
    )

    class Meta:
        per_page = 15
        model = Schedule
        fields = ['name', 'description']
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
