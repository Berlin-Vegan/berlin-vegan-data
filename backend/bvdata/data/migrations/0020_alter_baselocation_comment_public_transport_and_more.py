# Generated by Django 4.0.4 on 2022-05-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0019_add_review_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baselocation",
            name="comment_public_transport",
            field=models.TextField(
                blank=True, default="", verbose_name="Comment Public Transport"
            ),
        ),
        migrations.AlterField(
            model_name="baselocation",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="baselocation",
            name="postal_code",
            field=models.CharField(max_length=5, verbose_name="Postal Code"),
        ),
        migrations.AlterField(
            model_name="baselocation",
            name="submit_email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Submitter E-mail"
            ),
        ),
        migrations.AlterField(
            model_name="baselocation",
            name="vegan",
            field=models.IntegerField(
                choices=[
                    (2, "Ominvore (vegan labeled)"),
                    (4, "Vegetarian (vegan labeled)"),
                    (5, "Vegan"),
                ],
                verbose_name="Vegan Friendly",
            ),
        ),
    ]
