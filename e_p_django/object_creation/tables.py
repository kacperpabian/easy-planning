import django_tables2 as tables
# noinspection PyUnresolvedReferences
from start_page import models


class SubjectTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='button_templates/button_delete_subject.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='button_templates/button_edit_subject.html'
    )

    class Meta:
        model = models.Subject
        fields = ['name', 'short_name']
        attrs = {
            'class': 'table-condensed align-middle',
            'style': 'border-radius: 5px; \
            width: 50%; \
            margin: 0px auto; \
            float: none;'
        }


class RoomsTable(tables.Table):
    room_number = tables.Column(verbose_name='Numer pokoju')
    capacity = tables.Column(verbose_name='Liczba miejsc')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='button_templates/button_delete_room.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='button_templates/button_edit_room.html'
    )

    class Meta:
        model = models.Room
        fields = ['room_number', 'capacity']
        attrs = {
            'class': 'table-condensed align-middle',
            'style': 'border-radius: 5px; \
            width: 50%; \
            margin: 0px auto; \
            float: none;'
        }
