from django.db import models


class HR(models.Model):
    fio = models.CharField(max_length=256, verbose_name='ФИО')
    org_name = models.CharField(max_length=64, verbose_name='Название организации')
    org_email = models.CharField(max_length=64, verbose_name='Почта организации')
    org_type = models.CharField(max_length=64, verbose_name='Тип организации')
    excursion = models.BooleanField(verbose_name='Готовы ли проводить экскурсии')
    practices = models.BooleanField(verbose_name='Готовы ли проводить практики')
    event = models.BooleanField(verbose_name = 'Готовы ли участвовать в мероприятиях')

    def __str__(self):
        return f'{self.org_name} {self.fio}'
