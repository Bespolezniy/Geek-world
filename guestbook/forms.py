from django import forms
from guestbook.models import GuestBook

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = '__all__'

    user = forms.CharField(max_length = 15, label = "User")
    content = forms.CharField(widget = forms.Textarea, label="Content")
    honeypot = forms.CharField(widget = forms.HiddenInput, required = False, label="Trap")
