# Generated by Django 4.2.3 on 2025-02-13 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=13)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceRequest",
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
                ("request_type", models.CharField(max_length=100)),
                ("details", models.TextField()),
                (
                    "attachment",
                    models.FileField(blank=True, null=True, upload_to="attachment/"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In Progress"),
                            ("Resolved", "Resolved"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                ("submitted_date", models.DateTimeField(auto_now_add=True)),
                ("resolved_date", models.DateTimeField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Statement.customer",
                    ),
                ),
            ],
        ),
    ]
