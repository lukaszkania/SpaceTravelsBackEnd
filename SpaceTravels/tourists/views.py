from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
from .forms import TouristCreationForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class LogoutRequiredMixin():
    '''Class created to redirect logged in users from register and login pages'''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

class TouristCreateView(LogoutRequiredMixin ,CreateView):
    '''Our register page, containing register form from form.py file.'''
    template_name = 'tourists/Registration.html'
    form_class = TouristCreationForm # Our form from forms.py

    # Redirecting after login
    def get_success_url(self):
        return reverse('home')