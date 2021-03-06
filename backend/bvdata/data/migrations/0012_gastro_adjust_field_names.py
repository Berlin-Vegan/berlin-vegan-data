# Generated by Django 2.1.15 on 2020-07-10 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("data", "0011_remove_gastro_submit")]

    operations = [
        migrations.RenameField(
            model_name="gastro", old_name="childChair", new_name="child_chair"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingFri", new_name="closing_fri"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingMon", new_name="closing_mon"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingSat", new_name="closing_sat"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingSun", new_name="closing_sun"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingThu", new_name="closing_thu"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingTue", new_name="closing_tue"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="closingWed", new_name="closing_wed"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="commentEnglish", new_name="comment_english"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="commentOpen", new_name="comment_open"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="glutenFree", new_name="gluten_free"
        ),
        migrations.RenameField(
            model_name="gastro",
            old_name="handicappedAccessible",
            new_name="handicapped_accessible",
        ),
        migrations.RenameField(
            model_name="gastro",
            old_name="handicappedAccessibleWc",
            new_name="handicapped_accessible_wc",
        ),
        migrations.RenameField(
            model_name="gastro", old_name="latCoord", new_name="latitude"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="longCoord", new_name="longitude"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingFri", new_name="opening_fri"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingMon", new_name="opening_mon"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingSat", new_name="opening_sat"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingSun", new_name="opening_sun"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingThu", new_name="opening_thu"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingTue", new_name="opening_tue"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="openingWed", new_name="opening_wed"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="cityCode", new_name="postal_code"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="publicTransport", new_name="public_transport"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="seatsIndoor", new_name="seats_indoor"
        ),
        migrations.RenameField(
            model_name="gastro", old_name="seatsOutdoor", new_name="seats_outdoor"
        ),
    ]
