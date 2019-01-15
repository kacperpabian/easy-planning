from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django_tables2 import (
    SingleTableView,
    LazyPaginator
)


from .forms import RoomForm
from .models import Room
from .tables import RoomsTable
from school_schedule.models import School


class RoomCreate(generic.CreateView):
    model = Room
    template_name = "rooms/room_add.html"
    form_class = RoomForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(RoomCreate, self).form_valid(form)


class RoomsView(SingleTableView):
    model = Room
    template_name = 'rooms/rooms.html'
    table_class = RoomsTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(RoomsView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        school = get_object_or_404(School, id=self.kwargs.get('pk'))
        return Room.objects.filter(school_id=school.id)


class RoomDelete(generic.DeleteView):
    model = Room
    template_name = "rooms/room_delete.html"

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(RoomDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['room'] = get_object_or_404(Room, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:school_schedule:rooms:rooms', kwargs={'pk': school_id})


class RoomUpdate(generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "rooms/room_edit.html"
    template_name_suffix = '_update_form'

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if form.changed_data:
                room = form.save(commit=False)
                room.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")
        return render(request, self.template_name, {'form': form})
