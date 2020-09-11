from django.http import response
from django.shortcuts import render


def home(request):

    return render(request=request, template_name='common/home.html')
