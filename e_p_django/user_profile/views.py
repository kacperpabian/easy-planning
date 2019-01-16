from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class ProfileView(generic.UpdateView):
    """View for user registration"""
    form_class = forms.UserFormProfile
    template_name = 'user_profile/profile_view.html'
    template_name_suffix = '_update_form'

    # display blank form
    def get(self, request, **kwargs):
        user = self.request.user
        data = {'username': user.username, 'email': user.email,
                'first_name': user.first_name, 'last_name': user.last_name}
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            if form.changed_data:
                user = form.save(commit=False)
                user.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")

        return render(request, self.template_name, {'form': form})
