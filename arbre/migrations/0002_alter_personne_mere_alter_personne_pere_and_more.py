# Generated by Django 4.2.6 on 2023-11-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='mere',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='pere',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='user_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]