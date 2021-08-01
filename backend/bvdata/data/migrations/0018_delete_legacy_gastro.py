from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0017_migrate_legacy_gastro_baselocation"),
    ]

    operations = [
        migrations.CreateModel(
            name="LegacyGastro",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_string",
                    models.CharField(
                        blank=True, max_length=32, unique=True, verbose_name="unique id"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Name of location"),
                ),
                (
                    "street",
                    models.CharField(max_length=100, verbose_name="Street / No"),
                ),
                (
                    "postal_code",
                    models.CharField(max_length=5, verbose_name="Postal code"),
                ),
                (
                    "city",
                    models.CharField(
                        default="Berlin", max_length=20, verbose_name="City"
                    ),
                ),
                ("latitude", models.FloatField(verbose_name="latitude")),
                ("longitude", models.FloatField(verbose_name="longitude")),
                (
                    "telephone",
                    models.CharField(
                        blank=True, max_length=25, null=True, verbose_name="Telephone"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="E-mail"
                    ),
                ),
                (
                    "opening_mon",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening monday"
                    ),
                ),
                (
                    "closing_mon",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing monday"
                    ),
                ),
                (
                    "opening_tue",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening tuesday"
                    ),
                ),
                (
                    "closing_tue",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing tuesday"
                    ),
                ),
                (
                    "opening_wed",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening wednesday"
                    ),
                ),
                (
                    "closing_wed",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing wednesday"
                    ),
                ),
                (
                    "opening_thu",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening thursday"
                    ),
                ),
                (
                    "closing_thu",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing thursday"
                    ),
                ),
                (
                    "opening_fri",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening friday"
                    ),
                ),
                (
                    "closing_fri",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing friday"
                    ),
                ),
                (
                    "opening_sat",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening saturday"
                    ),
                ),
                (
                    "closing_sat",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing saturday"
                    ),
                ),
                (
                    "opening_sun",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening sunday"
                    ),
                ),
                (
                    "closing_sun",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing sunday"
                    ),
                ),
                (
                    "vegan",
                    models.IntegerField(
                        choices=[
                            (2, "Ominvore (vegan labeled)"),
                            (4, "Vegetarian (vegan labeled)"),
                            (5, "Vegan"),
                        ],
                        verbose_name="Vegan friendly",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, null=True, verbose_name="Comment in German"
                    ),
                ),
                (
                    "comment_english",
                    models.TextField(
                        blank=True, null=True, verbose_name="Comment in English"
                    ),
                ),
                (
                    "review_link",
                    models.URLField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="review link",
                    ),
                ),
                (
                    "closed",
                    models.DateField(default=None, null=True, verbose_name="closed"),
                ),
                (
                    "text_intern",
                    models.TextField(blank=True, null=True, verbose_name="text intern"),
                ),
                (
                    "district",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("CHARLOTTENBURG", "Charlottenburg"),
                            ("FRIEDRICHSHAIN", "Friedrichshain"),
                            ("HELLERSDORF", "Hellersdorf"),
                            ("HOHENSCHÖNHAUSEN", "Hohenschönhausen"),
                            ("KREUZBERG", "Kreuzberg"),
                            ("KÖPENICK", "Köpenick"),
                            ("LICHTENBERG", "Lichtenberg"),
                            ("MARZAHN", "Marzahn"),
                            ("MITTE", "Mitte"),
                            ("NEUKÖLLN", "Neukölln"),
                            ("PANKOW", "Pankow"),
                            ("PRENZLAUER BERG", "Prenzlauer Berg"),
                            ("REINICKENDORF", "Reinickendorf"),
                            ("SCHÖNEBERG", "Schöneberg"),
                            ("SPANDAU", "Spandau"),
                            ("STEGLITZ", "Steglitz"),
                            ("TEMPELHOF", "Tempelhof"),
                            ("TIERGARTEN", "Tiergarten"),
                            ("TREPTOW", "Treptow"),
                            ("WEDDING", "Wedding"),
                            ("WEISSENSEE", "Weißensee"),
                            ("WILMERSDORF", "Wilmersdorf"),
                            ("ZEHLENDORF", "Zehlendorf"),
                        ],
                        max_length=30,
                        null=True,
                        verbose_name="District",
                    ),
                ),
                (
                    "public_transport",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Public transport",
                    ),
                ),
                (
                    "handicapped_accessible",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Wheelchair accessible",
                    ),
                ),
                (
                    "handicapped_accessible_wc",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Wheelchair accessible toilet",
                    ),
                ),
                (
                    "dog",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Dogs allowed",
                    ),
                ),
                (
                    "child_chair",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="High chair",
                    ),
                ),
                (
                    "catering",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Catering",
                    ),
                ),
                (
                    "delivery",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Delivery service",
                    ),
                ),
                (
                    "organic",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Organic",
                    ),
                ),
                (
                    "wlan",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Wi-Fi",
                    ),
                ),
                (
                    "gluten_free",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Gluten-free options",
                    ),
                ),
                (
                    "breakfast",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Vegan Breakfast",
                    ),
                ),
                (
                    "brunch",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        null=True,
                        verbose_name="Brunch",
                    ),
                ),
                (
                    "seats_outdoor",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Seats outdoor"
                    ),
                ),
                (
                    "seats_indoor",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Seats indoor"
                    ),
                ),
                (
                    "restaurant",
                    models.BooleanField(default=False, verbose_name="Restaurant"),
                ),
                (
                    "imbiss",
                    models.BooleanField(default=False, verbose_name="Snack bar"),
                ),
                (
                    "eiscafe",
                    models.BooleanField(default=False, verbose_name="Ice cream parlor"),
                ),
                ("cafe", models.BooleanField(default=False, verbose_name="Café")),
                ("bar", models.BooleanField(default=False, verbose_name="Bar")),
                (
                    "comment_open",
                    models.TextField(
                        blank=True, null=True, verbose_name="Comment opening hours"
                    ),
                ),
                (
                    "submit_email",
                    models.EmailField(
                        blank=True,
                        default="",
                        max_length=254,
                        verbose_name="Submitter e-mail",
                    ),
                ),
                (
                    "has_sticker",
                    models.BooleanField(default=False, verbose_name="Sticker"),
                ),
                (
                    "is_submission",
                    models.BooleanField(default=True, verbose_name="Submission"),
                ),
            ],
            options={
                "db_table": "data_gastro",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Gastro",
        ),
    ]
