# Generated by Django 5.0.2 on 2024-03-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("date_hadis", "0006_rename_title_tr_post_title_ur"),
    ]

    operations = [
        migrations.AddField(
            model_name="block",
            name="text_en",
            field=models.TextField(blank=True, null=True, verbose_name="Block Text"),
        ),
        migrations.AddField(
            model_name="block",
            name="text_ur",
            field=models.TextField(blank=True, null=True, verbose_name="Block Text"),
        ),
    ]
