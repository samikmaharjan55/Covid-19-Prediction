# Generated by Django 4.0.3 on 2022-04-10 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19_predictor', '0003_alter_covidsymptoms_breath_alter_covidsymptoms_cough_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidsymptoms',
            name='breath',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='covidsymptoms',
            name='cough',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='covidsymptoms',
            name='fever',
            field=models.FloatField(),
        ),
    ]
