import django_tables2 as tables

from .models import Room


class RoomsTable(tables.Table):
    room_number = tables.Column(verbose_name='Numer pokoju')
    capacity = tables.Column(verbose_name='Liczba miejsc')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='rooms/button_delete_room.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='rooms/button_edit_room.html'
    )

    class Meta:
        model = Room
        fields = ['room_number', 'capacity']
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
