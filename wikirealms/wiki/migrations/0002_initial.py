# Generated by Django 4.1.7 on 2023-02-20 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("worldbuilding", "0001_initial"),
        ("main", "0002_initial"),
        ("wiki", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wikipage",
            name="realm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worldbuilding.realm"
            ),
        ),
        migrations.AddField(
            model_name="wikipage",
            name="users",
            field=models.ManyToManyField(to="main.profile"),
        ),
    ]
