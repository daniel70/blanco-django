from django.contrib import messages
from django.shortcuts import render


def home(request):
    messages.info(request, "Thank you for using Blanco-Django!")
    return render(request=request, template_name='common/home.html')
