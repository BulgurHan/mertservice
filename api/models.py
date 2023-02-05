from django.db import models


DURUM = [
    ('yeni','Yeni Başladı'),
    ('devam','Devam Ediyor'),
    ('bitti','Bitti')

]

ACİLİYET = [
    ('acil','Acil'),
    ('normal','Normal'),
    ('yok','Acelesi Yok')

]

class Proje(models.Model):
    baslik = models.CharField(max_length=55)
    bitirme_tarihi = models.DateField()
    durum = models.CharField(
        max_length=70,
        choices=DURUM
    )
    aciliyet = models.CharField(
        max_length=70,
        choices=ACİLİYET
    )
    konu = models.TextField()

