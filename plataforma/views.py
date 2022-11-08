from email import utils
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
    # elif request.method == "POST":
    #     ordem = request.POST.get('ordem')
    #     nota = request.POST.get('nota')
    #     cod_local_inst = request.POST.get('cod_local_inst')
    #     local_inst = request.POST.get('local_inst')
    #     tipo_insp = request.POST.get('tipo_insp')
    #     mes = request.POST.get('mes')
    #     status = request.POST.get('status')
    #     equipamento = request.POST.get('equipamento')

    #     try:
    #         p1 = PlanoManut(
    #         ordem = ordem,
    #         nota = nota,
    #         cod_local_inst = cod_local_inst,
    #         local_inst = local_inst,
    #         tipo_insp = tipo_insp,
    #         mes = mes,
    #         status = status,
    #         equipamento = equipamento
    #     )
    #         p1.save()
    #         messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso')
    #         return redirect('/')
    #     except:
    #         messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
    #         return redirect('/')


def filtrar(request):
    # return HttpResponse('FILTRAR')
    if request.method == 'POST':
        # return HttpResponse('Tela Plano de Manutenção')
        ordem = request.POST.get('ordem')
        if ordem == "":
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/')
        inspecoes = PlanoManut.objects.filter(ordem=ordem)
        return render(request, 'plano_manut.html', {'inspecao': inspecoes})



















# # importar os dados do csv
# import csv

# def upload(request):
#     with open(r'C:\Users\U1106811\Documents\CsvPmAtPython.csv', newline='') as f:
#         reader = csv.reader(f, delimiter=';')
#         dados = list(reader)
#         for i in dados:
#             p1 = PlanoManut(
#                 ordem = i[0],
#                 nota = i[1],
#                 cod_local_inst = i[2],
#                 local_inst = i[3],
#                 tipo_insp = i[4],
#                 mes = i[5],
#                 status = i[6],
#                 equipamento = i[7]
#             )
            
#             p1.save()

#             print('Ok, inserido ordem '+i[0])