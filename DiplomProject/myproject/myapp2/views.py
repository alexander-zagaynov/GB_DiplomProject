import logging

from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Используем эти  данные
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
        return render(request, 'myapp2/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp2/many_fields_form.html',
    {'form': form})
# Create your views here.
