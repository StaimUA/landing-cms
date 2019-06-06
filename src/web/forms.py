from django.forms import ModelForm

from .models import ContactForm

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Your E-mail'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Your Full Name'
        self.fields['comment'].widget.attrs['placeholder'] = 'Your comments'

    class Meta:
        model = ContactForm
        fields = ['email', 'full_name', 'comment']
