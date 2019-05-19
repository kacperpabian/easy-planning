from django import forms

from .models import Lesson
from schedules.models import Schedule
from schools.models import School


class LessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        work_dict = kwargs.pop('work_dict', None)
        max_lessons = kwargs.pop('max_lessons', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if work_dict:
            work_dict = ((str(key), value) for key, value in work_dict.items())
            if work_dict:
                self.fields['day'] = forms.ChoiceField(required=True, choices=work_dict,
                                                       widget=forms.Select(), label="Dzień")
        if max_lessons:
            max_lessons = ((i, i) for i in range(1, max_lessons + 1))
            if max_lessons:
                self.fields['lesson_number'] = forms.ChoiceField(required=True, choices=max_lessons,
                                                                 widget=forms.Select(), label="Numer lekcji")

    class Meta:
        labels = {
            'group': 'Grupa',
            'subject': 'Przedmiot',
            'teacher': 'Prowadzący',
            'room': 'Pokój',
            'lesson_number': 'Numer lekcji',
            'day': 'Dzień'
        }
        model = Lesson
        fields = ['group', 'subject', 'teacher', 'room', 'lesson_number', 'day']


class ScheduleCombo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        school_pk = kwargs.pop('school_pk', None)
        class_id = kwargs.pop('class_id', None)
        schedule_id = kwargs.pop('schedule_id', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if school_pk is not None:
            school = School.objects.get(id=school_pk)
            class_field = self.fields['class_field']
            class_field.queryset = school.class_set.all()
            if class_id:
                class_field.initial = class_id
            schedule_field = self.fields['schedule']
            if schedule_id and class_id:
                schedule_field.queryset = Schedule.objects.filter(class_field_id=int(class_id))
                schedule_field.initial = schedule_id
            else:
                schedule_field.queryset = school.schedule_set.none()

        if 'schedule' in self.data:
            try:
                class_id = int(self.data.get('class_field'))
                self.fields['schedule'].queryset = Schedule.objects.filter(class_field_id=class_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['schedule'].queryset = self.instance.class_field.schedule_set.order_by('name')

    class Meta:
        labels = {
            'class_field': 'Klasa',
            'schedule': 'Rok'
        }
        model = Lesson
        fields = ['class_field', 'schedule']

# class ScheduleCombo(forms.Form):
#     schedules = None
#
#     def __init__(self, *args, **kwargs):
#         self.school_id = kwargs.pop('school_id')
#         super(ScheduleCombo, self).__init__(*args, **kwargs)
#         self.schedules = Schedule.objects.all().filter(school_id=self.school_id)
#
#     forms.ModelChoiceField(queryset=schedules)
