# Generated by Django 4.0.3 on 2022-04-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChanceCovid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chance', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CovidSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cough', models.DecimalField(decimal_places=10, max_digits=10)),
                ('fever', models.DecimalField(decimal_places=10, max_digits=10)),
                ('breath', models.DecimalField(decimal_places=10, max_digits=10)),
                ('age_field', models.IntegerField()),
                ('environment', models.IntegerField()),
                ('hypertension', models.IntegerField()),
                ('diabetes', models.IntegerField()),
                ('cardiovascular', models.IntegerField()),
                ('respiratory', models.IntegerField()),
                ('immune', models.IntegerField()),
            ],
        ),
    ]
