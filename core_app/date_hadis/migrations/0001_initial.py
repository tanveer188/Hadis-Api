# Generated by Django 5.0.2 on 2024-03-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Block",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="block_images/"),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("text", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("date", models.DateField()),
                ("title", models.CharField(max_length=30)),
                ("blocks", models.ManyToManyField(to="date_hadis.block")),
            ],
        ),
    ]
