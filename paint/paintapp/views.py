from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader


# Create your views here.
def paint(request):
    template = loader.get_template('paintapp/paint.html')
    context = {}
    return HttpResponse(template.render(context, request))