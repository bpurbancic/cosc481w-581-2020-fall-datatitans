# Generated by Django 3.1.2 on 2020-11-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20201021_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='coviddataraw',
            name='hosp_patients',
            field=models.IntegerField(db_column='hosp_patients', null=True, verbose_name='hospital patients'),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='hosp_patients_per_million',
            field=models.FloatField(db_column='hosp_patients_per_million', null=True, verbose_name='hospital patients per million'),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='icu_patients',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='icu_patients_per_million',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='weekly_hosp_admissions',
            field=models.FloatField(db_column='weekly_hosp_admissions', null=True, verbose_name='weekly hospital admissions'),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='weekly_hosp_admissions_per_million',
            field=models.FloatField(db_column='weekly_hosp_admissions_per_million', null=True, verbose_name='weekly hospital admissions per million'),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='weekly_icu_admissions',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='coviddataraw',
            name='weekly_icu_admissions_per_million',
            field=models.FloatField(null=True),
        ),
    ]
