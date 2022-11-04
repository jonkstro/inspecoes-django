from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import PlanoManut
from django.contrib import messages
from django.contrib.messages import constants



def plano_manut(request):
    if request.method == 'GET':
        # return HttpResponse('Tela Plano de Manutenção')
        inspecoes = PlanoManut.objects.all()
        return render(request, 'plano_manut.html', {'inspecao': inspecoes})
    elif request.method == "POST":
        ordem = request.POST.get('ordem')
        nota = request.POST.get('nota')
        cod_local_inst = request.POST.get('cod_local_inst')
        local_inst = request.POST.get('local_inst')
        tipo_insp = request.POST.get('tipo_insp')
        mes = request.POST.get('mes')
        status = request.POST.get('status')
        equipamento = request.POST.get('equipamento')

        try:
            p1 = PlanoManut(
            ordem = ordem,
            nota = nota,
            cod_local_inst = cod_local_inst,
            local_inst = local_inst,
            tipo_insp = tipo_insp,
            mes = mes,
            status = status,
            equipamento = equipamento
        )
            p1.save()
            messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso')
            return redirect('/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/')

