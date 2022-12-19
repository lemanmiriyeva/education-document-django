from django.shortcuts import render
import json
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4
from datetime import datetime

# Create your views here.
class FormView(FormView):
    template_name="form.html"
    form_class=UserForm
    success_url="/detail/"
    form=UserForm()
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DetailView(TemplateView):
    template_name="information.html"
    model=UserDetail
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["user"]=UserDetail.objects.last()
        return context


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'user':UserDetail.objects.filter(id=self.kwargs['pk']).first()
             
        }
        pdf = render_to_pdf('pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')