# Generated by Django 4.2.6 on 2023-11-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbre', '0003_personne_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='sexe',
            field=models.CharField(blank=True, choices=[('homme', 'homme'), ('femme', 'femme')], max_length=40),
        ),
    ]
