
from django.http import HttpResponse
from django.template import loader

def health_check (request):
    template = loader.get_template('public/health_check.html')
    return HttpResponse(
        template.render()
    )
