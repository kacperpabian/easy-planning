import django_tables2 as tables
# noinspection PyUnresolvedReferences
from start_page import models


class ScheduleTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa planu')
    description = tables.Column(verbose_name='Opis')
    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='button_templates/button_delete_schedule.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='button_templates/button_edit_schedule.html'
    )

    class Meta:
        model = models.Schedule
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


class TeacherTable(tables.Table):
    name = tables.Column(verbose_name='Imię')
    surname = tables.Column(verbose_name='Nazwisko')

    deatils = tables.TemplateColumn(
        verbose_name='Szczegóły',
        template_name='button_templates/button_details_teacher.html'
    )

    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='button_templates/button_delete_teacher.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='button_templates/button_edit_teacher.html'
    )

    class Meta:
        model = models.Teacher
        fields = ['name', 'surname']
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


class ClassTable(tables.Table):
    name = tables.Column(verbose_name='Nazwa')
    short_name = tables.Column(verbose_name='Skrócona nazwa')

    deatils = tables.TemplateColumn(
        verbose_name='Szczegóły',
        template_name='button_templates/button_details_class.html'
    )

    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='button_templates/button_delete_class.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='button_templates/button_edit_class.html'
    )

    class Meta:
        model = models.Class
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
