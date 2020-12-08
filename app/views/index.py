from django.shortcuts import render

from app.models import Traxxas


def index(request):
    if Traxxas.objects.exists():
        traxxas = Traxxas.objects.all()
        context = {
            'traxxas': traxxas,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
