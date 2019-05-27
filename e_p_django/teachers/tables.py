import django_tables2 as tables

from .models import Teacher


class TeacherTable(tables.Table):
    name = tables.Column(verbose_name='Imię')
    surname = tables.Column(verbose_name='Nazwisko')

    # deatils = tables.TemplateColumn(
    #     verbose_name='Szczegóły',
    #     template_name='teachers/button_details_teacher.html'
    # )

    delete = tables.TemplateColumn(
        verbose_name='Usuń',
        template_name='teachers/button_delete_teacher.html'
    )

    edit = tables.TemplateColumn(
        verbose_name='Edytuj',
        template_name='teachers/button_edit_teacher.html'
    )

    class Meta:
        model = Teacher
        per_page = 15
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
