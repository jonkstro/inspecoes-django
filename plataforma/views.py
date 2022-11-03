from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PlanoManut

def plano_manut(request):
    if request.method == 'GET':
        # return HttpResponse('Tela Plano de Manutenção')
        inspecoes = PlanoManut.objects.all()
        return render(request, 'plano_manut.html', {'inspecao': inspecoes})


# pacientes = Pacientes.objects.filter(nutri=request.user)
# return render(request, 'pacientes.html', {'pacientes': pacientes})