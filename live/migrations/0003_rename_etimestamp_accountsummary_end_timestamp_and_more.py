# Generated by Django 4.2.7 on 2024-04-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("live", "0002_rename_end_timestamp_accountsummary_etimestamp_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="accountsummary",
            old_name="etimestamp",
            new_name="end_timestamp",
        ),
        migrations.RenameField(
            model_name="accountsummary",
            old_name="stimestamp",
            new_name="start_timestamp",
        ),
    ]