# Generated by Django 3.0.5 on 2020-05-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alimentacion", "0005_auto_20200526_1748"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alimentacion",
            name="lista_negra",
            field=models.CharField(
                choices=[("0", "No"), ("1", "Si")], default="No", max_length=2
            ),
        ),
    ]
