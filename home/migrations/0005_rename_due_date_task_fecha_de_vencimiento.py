# Generated by Django 4.2 on 2023-04-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_task_priority_task_prioridad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='fecha_de_vencimiento',
        ),
    ]