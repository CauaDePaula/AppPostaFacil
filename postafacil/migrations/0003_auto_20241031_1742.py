# Generated by Django 3.2.8 on 2024-10-31 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("postafacil", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=2)),
                ("cep", models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name="client",
            name="city",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients",
                to="postafacil.city",
            ),
        ),
    ]
