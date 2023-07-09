# Generated by Django 4.2.2 on 2023-06-30 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.departamento'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
