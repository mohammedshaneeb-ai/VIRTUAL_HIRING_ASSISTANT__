# Generated by Django 4.2.4 on 2023-08-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_candidate_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="domain",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
