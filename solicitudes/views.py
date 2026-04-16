from django.shortcuts import render, redirect
from .forms import SolicitudForm

def registro_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_solicitud')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/registro.html', {'form': form})

def confirmacion_solicitud(request):
    return render(request, 'solicitudes/confirmacion.html')