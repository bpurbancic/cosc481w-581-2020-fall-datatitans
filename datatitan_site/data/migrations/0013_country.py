# Generated by Django 3.1.3 on 2020-11-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("data", "0012_auto_20201116_1347"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "iso_code",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=55)),
                ("continent", models.CharField(max_length=15)),
                ("population", models.FloatField()),
            ],
        ),
    ]
