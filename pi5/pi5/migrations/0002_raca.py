# Generated by Django 4.2.1 on 2023-05-30 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pi5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi5.tipo')),
            ],
            options={
                'verbose_name': 'Raça',
                'verbose_name_plural': 'Raças',
            },
        ),
    ]
