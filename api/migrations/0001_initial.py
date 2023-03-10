# Generated by Django 4.0.3 on 2023-02-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=55)),
                ('bitirme_tarihi', models.DateField()),
                ('durum', models.CharField(choices=[('yeni', 'Yeni Başladı'), ('devam', 'Devam Ediyor'), ('bitti', 'Bitti')], max_length=70)),
                ('aciliyet', models.CharField(choices=[('acil', 'Acil'), ('normal', 'Normal'), ('yok', 'Acelesi Yok')], max_length=70)),
                ('konu', models.TextField()),
            ],
        ),
    ]
