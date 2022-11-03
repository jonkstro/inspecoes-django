from django.db import models


class PlanoManut(models.Model):
    ordem = models.IntegerField()
    nota = models.IntegerField()
    cod_local_inst = models.CharField(max_length=15)
    local_inst = models.CharField(max_length=50)
    tipo_insp = models.CharField(max_length=20)
    mes = models.DateField()
    status = models.CharField(max_length=20)
    equipamento = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Local({self.cod_local_inst}, {self.ordem})"


class Inspecao(models.Model):
    ordem = models.ForeignKey(PlanoManut, on_delete=models.CASCADE)
    si = models.IntegerField()
    data_inic = models.DateField()
    hora_inic = models.TimeField()
    data_fim = models.DateField()
    hora_fim = models.TimeField()
    tempo_desloc = models.FloatField()
    tempo_trab = models.FloatField()
    tempo_escrit = models.FloatField()
    is_lac = models.BooleanField()

    def __str__(self):
        return self.ordem.ordem


class Validacao(models.Model):
    ordem = models.ForeignKey(PlanoManut, on_delete=models.CASCADE)
    is_inspec = models.BooleanField()
    is_sap = models.BooleanField()

    def __str__(self):
        return self.ordem.ordem