from django.views.generic import TemplateView, ListView
from django.views.generic.edit import ModelFormMixin

from .models import Block
from .forms import ContactForm


class IndexView(ListView, ModelFormMixin):
    template_name = 'index.html'
    model = Block
    form_class = ContactForm
    context_object_name = 'block_list'
    queryset = Block.objects.all().prefetch_related('skill_list', 'team_list', 'portfolio_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form
        return ctx
