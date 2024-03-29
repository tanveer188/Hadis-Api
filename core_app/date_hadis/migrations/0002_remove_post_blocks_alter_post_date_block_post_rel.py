# Generated by Django 5.0.2 on 2024-03-03 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("date_hadis", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="blocks",
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(unique=True),
        ),
        migrations.CreateModel(
            name="Block_Post_Rel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "block",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="date_hadis.block",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="date_hadis.post",
                    ),
                ),
            ],
            options={
                "ordering": ["post", "order"],
                "unique_together": {("post", "block")},
            },
        ),
    ]
