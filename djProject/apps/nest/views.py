# Create your views here.
from django.template.response import TemplateResponse



def home(request):
    return TemplateResponse(request, 'index.html', {})