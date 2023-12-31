# Generated by Django 4.2.6 on 2023-11-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_settings", "0004_rename_footerconent_footercontent"),
    ]

    operations = [
        migrations.RenameField(
            model_name="footercontent",
            old_name="footer_content",
            new_name="content",
        ),
        migrations.AddField(
            model_name="footercontent",
            name="title",
            field=models.TextField(
                blank=True, help_text="Enter Footer Content Title here"
            ),
        ),
    ]
