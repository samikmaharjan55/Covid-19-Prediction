# Generated by Django 4.0.3 on 2022-04-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19_predictor', '0005_alter_covidsymptoms_breath_alter_covidsymptoms_cough_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chancecovid',
            name='chance',
            field=models.IntegerField(),
        ),
    ]