from apps.models import *
from wtforms import Form
from wtforms_alchemy import model_form_factory

ModelForm = model_form_factory(Form)


class BookForm(ModelForm):
    class Meta:
        model = Book
