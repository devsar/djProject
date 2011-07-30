# Create your views here.
from django.template.response import TemplateResponse

def main(request):
    
    return TemplateResponse(request, "projects/main.html", {})

    