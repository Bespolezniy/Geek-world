from goods.models import Good
from django import forms

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = '__all__'