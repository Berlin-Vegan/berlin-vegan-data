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
    ]
