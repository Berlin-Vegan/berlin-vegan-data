from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("data", "0008_gastro_submit_email")]

    operations = [
        migrations.AddField(
            model_name="gastro",
            name="is_submission",
            field=models.BooleanField(default=True, verbose_name="Submission"),
        ),
        migrations.AlterField(
            model_name="gastro",
            name="district",
            field=models.CharField(
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
    ]
