from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0015_refactor_baselocation"),
    ]

    operations = [
        migrations.CreateModel(
            name="PositiveIntegerAttribute",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("seats_outdoor", "Seats Outdoor"),
                            ("seats_indoor", "Seats Indoor"),
                        ],
                        max_length=13,
                    ),
                ),
                ("state", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="baselocation",
            name="comment_public_transport",
            field=models.TextField(
                blank=True, default="", verbose_name="Comment Public transport"
            ),
        ),
        migrations.AddConstraint(
            model_name="positiveintegerattribute",
            constraint=models.CheckConstraint(
                check=models.Q(("name__in", ["seats_outdoor", "seats_indoor"])),
                name="data_positiveintegerattribute_name_valid",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="positiveintegerattribute",
            unique_together={("name", "state")},
        ),
        migrations.AddField(
            model_name="baselocation",
            name="positive_integer_attributes",
            field=models.ManyToManyField(to="data.PositiveIntegerAttribute"),
        ),
        migrations.RemoveConstraint(
            model_name="booleanattribute",
            name="data_booleanattribute_name_valid",
        ),
        migrations.AlterField(
            model_name="booleanattribute",
            name="name",
            field=models.CharField(
                choices=[
                    ("organic", "Organic"),
                    ("delivery", "Delivery"),
                    ("handicapped_accessible", "Handicapped Accessible"),
                    ("webshop", "Webshop"),
                    ("organic", "Organic"),
                    ("delivery", "Delivery"),
                    ("handicapped_accessible", "Handicapped Accessible"),
                    ("handicapped_accessible_wc", "Handicapped Accessible WC"),
                    ("dog", "Dog"),
                    ("child_chair", "Child Chair"),
                    ("catering", "Catering"),
                    ("wlan", "Wlan"),
                    ("gluten_free", "Gluten Free"),
                    ("breakfast", "Breakfast"),
                    ("brunch", "Brunch"),
                ],
                max_length=25,
            ),
        ),
        migrations.AddConstraint(
            model_name="booleanattribute",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "name__in",
                        [
                            "organic",
                            "delivery",
                            "handicapped_accessible",
                            "webshop",
                            "organic",
                            "delivery",
                            "handicapped_accessible",
                            "handicapped_accessible_wc",
                            "dog",
                            "child_chair",
                            "catering",
                            "wlan",
                            "gluten_free",
                            "breakfast",
                            "brunch",
                        ],
                    )
                ),
                name="data_booleanattribute_name_valid",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="tag",
            field=models.CharField(
                choices=[
                    ("foods", "Foods"),
                    ("clothing", "Clothing"),
                    ("toiletries", "Toiletries"),
                    ("supermarket", "Supermarket"),
                    ("hairdressers", "Hairdressers"),
                    ("sports", "Sports"),
                    ("tattoostudio", "Tattoostudio"),
                    ("accommodation", "Accommodation"),
                    ("bar", "Bar"),
                    ("cafe", "Cafe"),
                    ("ice cream parlor", "Ice Cream Parlor"),
                    ("snack bar", "Snack Bar"),
                    ("restaurant", "Restaurant"),
                ],
                max_length=16,
                unique=True,
            ),
        ),
    ]
