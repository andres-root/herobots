from django.forms import ModelForm
from .models import Preorder


class PreorderForm(ModelForm):
    class Meta:
        model = Preorder
        exclude = ['active', 'date_created', 'date_updated']
