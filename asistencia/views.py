from django.shortcuts import redirect, render

from .forms import AsistenciaForm


def registro_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_asistencia')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/registro.html', {'form': form})


def confirmacion_asistencia(request):
    return render(request, 'asistencia/confirmacion.html')
