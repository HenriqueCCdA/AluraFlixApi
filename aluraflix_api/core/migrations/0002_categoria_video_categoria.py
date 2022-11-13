# Generated by Django 4.1.3 on 2022-11-13 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('titulo', models.CharField(max_length=60)),
                ('cor', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='videos',
                to='core.categoria',
            ),
        ),
    ]
