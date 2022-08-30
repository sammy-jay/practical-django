from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import FormView
from main import forms


def home(request):
    return render(request, 'main/home.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def contact_us(request):
    if request.method == 'POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return redirect(reverse('main:home'))
    else:
        form = forms.ContactUsForm()
    return render(request, 'main/contact.html', {'form': form})


class ContactUsView(FormView):
    template_name = 'main/contact.html'
    form_class = forms.ContactUsForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
