from django.forms import ModelForm

from .models import ContactForm

class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['email', 'full_name', 'comment']
