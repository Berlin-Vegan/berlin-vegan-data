# Generated by Django 3.0.8 on 2020-09-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("data", "0012_gastro_adjust_field_names")]

    operations = [
        migrations.AlterField(
            model_name="gastro",
            name="breakfast",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Vegan Breakfast",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="brunch",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Brunch",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="catering",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Catering",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="child_chair",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="High chair",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="delivery",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Delivery service",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="dog",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Dogs allowed",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="gluten_free",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Gluten-free options",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="handicapped_accessible",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Wheelchair accessible",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="handicapped_accessible_wc",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Wheelchair accessible toilet",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="organic",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Organic",
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="review_link",
            field=models.URLField(
                blank=True, default="", max_length=255, verbose_name="review link"
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="submit_email",
            field=models.EmailField(
                blank=True, default="", max_length=254, verbose_name="Submitter e-mail"
            ),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="wlan",
            field=models.BooleanField(
                blank=True,
                choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                null=True,
                verbose_name="Wi-Fi",
            ),
        ),
    ]