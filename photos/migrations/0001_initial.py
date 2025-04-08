# Generated by Django 5.2 on 2025-04-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images/")),
                ("tags", models.ManyToManyField(related_name="photos", to="tags.tag")),
            ],
        ),
    ]
