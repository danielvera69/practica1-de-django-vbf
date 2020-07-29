from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm
from .models import Contacto


def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blogs'}

    return render(request, 'principal.html', opciones)


def acerca(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog'}
    # return HttpResponse('Acerca de...')
    return render(request, 'acerca.html', opciones)


def contacto(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcontacto')
    else:
        form = ContactoForm()
        opciones['form'] = form

    return render(request, 'contacto.html', opciones)


def editarContacto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    contacto = Contacto.objects.get(id=id)
    if request.method == 'GET':
        form = ContactoForm(instance=contacto)
        opciones['form'] = form
    else:
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listarcontacto')

    return render(request, 'contacto.html', opciones)


def listarContacto(request):
    contacto = Contacto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'contactos': contacto}
    return render(request, 'listar_contacto.html', opciones)


def eliminarContacto(request, id):
    contacto = Contacto.objects.get(id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listarcontacto')
    return render(request, 'eliminar_contacto.html', {'Contacto': contacto})
