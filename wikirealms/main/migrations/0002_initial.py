# Generated by Django 4.1.3 on 2023-01-07 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0001_initial"),
        ("wiki", "0002_initial"),
        ("worldbuilding", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
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
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
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
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
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
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="media_projects",
            field=models.ManyToManyField(to="wiki.mediaproject"),
        ),
        migrations.AddField(
            model_name="user",
            name="realms",
            field=models.ManyToManyField(
                through="main.UserRealmsAccess", to="worldbuilding.realm"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="theme",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="main.theme"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]