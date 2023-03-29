# Generated by Django 4.1.7 on 2023-03-28 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rutinas", "0005_remove_rutina_dias_dia_rutina"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dia",
            name="ejercicios",
        ),
        migrations.AddField(
            model_name="ejercicio",
            name="dia",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ejercicios",
                to="rutinas.dia",
            ),
        ),
    ]