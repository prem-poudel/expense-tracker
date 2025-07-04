# Generated by Django 5.2.4 on 2025-07-04 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("CR", "credit"), ("DB", "debit")],
                        default="DB",
                        max_length=2,
                    ),
                ),
                ("tax", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                (
                    "tax_type",
                    models.CharField(
                        choices=[("FL", "flat"), ("PE", "percentage")],
                        default="FL",
                        max_length=2,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
