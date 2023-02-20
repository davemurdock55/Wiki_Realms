# Generated by Django 4.1.7 on 2023-02-20 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("worldbuilding", "0001_initial"),
        ("main", "0001_initial"),
        ("wiki", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="userrealmsaccess",
            name="realm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worldbuilding.realm"
            ),
        ),
        migrations.AddField(
            model_name="userrealmsaccess",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.profile"
            ),
        ),
        migrations.AddField(
            model_name="userpageaccess",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worldbuilding.page"
            ),
        ),
        migrations.AddField(
            model_name="userpageaccess",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.profile"
            ),
        ),
        migrations.AddField(
            model_name="usermediaprojectaccess",
            name="media_project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wiki.mediaproject"
            ),
        ),
        migrations.AddField(
            model_name="usermediaprojectaccess",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.profile"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="media_projects",
            field=models.ManyToManyField(to="wiki.mediaproject"),
        ),
        migrations.AddField(
            model_name="profile",
            name="realms",
            field=models.ManyToManyField(
                through="main.UserRealmsAccess", to="worldbuilding.realm"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="theme",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="main.theme"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
