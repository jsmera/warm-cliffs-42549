# Generated by Django 3.0.5 on 2020-05-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_paciente"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="direccion",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="num_documento",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="telefono",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="direccion",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="num_documento",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="telefono",
            field=models.CharField(max_length=50),
        ),
    ]
