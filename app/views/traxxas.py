from django.shortcuts import render, redirect

from app.forms.traxxas import TraxxasForm, DeleteTraxxasForm
from app.models import Traxxas


def create_traxxas(request):
    if request.method == 'GET':
        context = {
            'form': TraxxasForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = TraxxasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def edit_traxxas(request, pk):
    traxxas = Traxxas.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'traxxas': traxxas,
            'form': TraxxasForm(instance=traxxas),
        }
        return render(request, 'edit.html', context)
    else:
        form = TraxxasForm(request.POST, instance=traxxas)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'traxxas': traxxas,
            'form': form,
        }
        return render(request, 'create.html', context)


def delete_traxxas(request, pk):
    traxxas = Traxxas.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'traxxas': traxxas,
            'form': DeleteTraxxasForm(instance=traxxas),
        }
        return render(request, 'delete.html', context)
    else:
        traxxas.delete()
        return redirect('index')


def details_traxxas(request, pk):
    if Traxxas.objects.exists():
        traxxas = Traxxas.objects.get(pk=pk)
        context = {
            'traxxas': traxxas,
        }
        return render(request, 'details.html', context)

