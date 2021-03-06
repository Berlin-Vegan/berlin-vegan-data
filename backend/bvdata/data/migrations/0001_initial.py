# Generated by Django 2.0 on 2018-01-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gastro",
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
                    models.CharField(max_length=100, verbose_name="location name"),
                ),
                ("street", models.CharField(max_length=100, verbose_name="street")),
                ("cityCode", models.CharField(max_length=5, verbose_name="citycode")),
                ("city", models.CharField(max_length=20, verbose_name="city")),
                ("latCoord", models.FloatField(verbose_name="latitude")),
                ("longCoord", models.FloatField(verbose_name="longitude")),
                (
                    "telephone",
                    models.CharField(
                        blank=True, max_length=25, null=True, verbose_name="telephone"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="website"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="email"
                    ),
                ),
                (
                    "openingMon",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening monday"
                    ),
                ),
                (
                    "closingMon",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing monday"
                    ),
                ),
                (
                    "openingTue",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening tuesday"
                    ),
                ),
                (
                    "closingTue",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing tuesday"
                    ),
                ),
                (
                    "openingWed",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening wednesday"
                    ),
                ),
                (
                    "closingWed",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing wednesday"
                    ),
                ),
                (
                    "openingThu",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening thursday"
                    ),
                ),
                (
                    "closingThu",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing thursday"
                    ),
                ),
                (
                    "openingFri",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening friday"
                    ),
                ),
                (
                    "closingFri",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing friday"
                    ),
                ),
                (
                    "openingSat",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening saturday"
                    ),
                ),
                (
                    "closingSat",
                    models.TimeField(
                        blank=True, null=True, verbose_name="closing saturday"
                    ),
                ),
                (
                    "openingSun",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening monday"
                    ),
                ),
                (
                    "closingSun",
                    models.TimeField(
                        blank=True, null=True, verbose_name="opening monday"
                    ),
                ),
                (
                    "vegan",
                    models.IntegerField(
                        choices=[
                            (2, "omnivore (vegan declared)"),
                            (4, "vegetarian (vegan declared)"),
                            (5, "100% vegan"),
                        ],
                        verbose_name="vegan",
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="comment"),
                ),
                (
                    "commentEnglish",
                    models.TextField(
                        blank=True, null=True, verbose_name="comment english"
                    ),
                ),
                (
                    "review_link",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="review link",
                    ),
                ),
                ("closed", models.BooleanField(default=False, verbose_name="closed")),
                (
                    "text_intern",
                    models.TextField(blank=True, null=True, verbose_name="text intern"),
                ),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("MITTE", "Mitte"),
                            ("TIERGARTEN", "Tiergarten"),
                            ("WEDDING", "Wedding"),
                            ("PRENZLAUER BERG", "Prenzlauer Berg"),
                            ("FRIEDRICHSHAIN", "Friedrichshain"),
                            ("KREUZBERG", "Kreuzberg"),
                            ("CHARLOTTENBURG", "Charlottenburg"),
                            ("SPANDAU", "Spandau"),
                            ("WILMERSDORF", "Wilmersdorf"),
                            ("ZEHLENDORF", "Zehlendorf"),
                            ("SCHÖNEBERG", "Schöneberg"),
                            ("STEGLITZ", "Steglitz"),
                            ("TEMPELHOF", "Tempelhof"),
                            ("NEUKÖLLN", "Neukölln"),
                            ("TREPTOW", "Treptow"),
                            ("KÖPENICK", "Köpenick"),
                            ("LICHTENBERG", "Lichtenberg"),
                            ("WEISSENSEE", "Weißensee"),
                            ("PANKOW", "Pankow"),
                            ("REINICKENDORF", "Reinickendorf"),
                            ("MARZAHN", "Marzahn"),
                            ("HOHENSCHÖNHAUSEN", "Hohenschönhausen"),
                            ("HELLERSDORF", "Hellersdorf"),
                        ],
                        max_length=30,
                        null=True,
                        verbose_name="district",
                    ),
                ),
                (
                    "publicTransport",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="public transport",
                    ),
                ),
                (
                    "handicappedAccessible",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="handicapped accessible",
                    ),
                ),
                (
                    "handicappedAccessibleWc",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="handicapped accessible wc",
                    ),
                ),
                (
                    "dog",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="dog",
                    ),
                ),
                (
                    "childChair",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="child's chair",
                    ),
                ),
                (
                    "catering",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="catering",
                    ),
                ),
                (
                    "delivery",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="delivery",
                    ),
                ),
                (
                    "organic",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="organic",
                    ),
                ),
                (
                    "wlan",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="wlan",
                    ),
                ),
                (
                    "glutenFree",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="gluten free",
                    ),
                ),
                (
                    "breakfast",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="breakfast",
                    ),
                ),
                (
                    "brunch",
                    models.NullBooleanField(
                        choices=[(None, "unknown"), (True, "yes"), (False, "no")],
                        verbose_name="brunch",
                    ),
                ),
                (
                    "seatsOutdoor",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="seats outdoor"
                    ),
                ),
                (
                    "seatsIndoor",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="seats indoor"
                    ),
                ),
                (
                    "restaurant",
                    models.BooleanField(default=False, verbose_name="restaurant"),
                ),
                ("imbiss", models.BooleanField(default=False, verbose_name="takeaway")),
                (
                    "eiscafe",
                    models.BooleanField(default=False, verbose_name="ice cream parlor"),
                ),
                (
                    "cafe",
                    models.BooleanField(default=False, verbose_name="coffee shop"),
                ),
                ("bar", models.BooleanField(default=False, verbose_name="bar")),
            ],
            options={"abstract": False},
        )
    ]
