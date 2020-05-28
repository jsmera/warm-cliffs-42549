# Generated by Django 3.0.5 on 2020-05-27 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("alimentacion", "0006_auto_20200527_1943"),
        ("historias", "0004_auto_20200526_1726"),
    ]

    operations = [
        migrations.CreateModel(
            name="LineaAlegia",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "causa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="alimentacion.Alimentacion",
                    ),
                ),
                (
                    "hisotoria_clinica",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="historias.HistoriaClinica",
                    ),
                ),
            ],
        ),
    ]
