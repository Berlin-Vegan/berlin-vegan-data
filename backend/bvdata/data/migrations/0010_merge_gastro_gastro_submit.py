from django.db import migrations

from bvdata.data.utils import get_random_string_32


def get_valid_id_string(model):
    id_string = get_random_string_32()
    if model.objects.filter(id_string=id_string).count() == 0:
        return id_string
    else:
        return get_valid_id_string(model)


def merge_gastro_gastro_submit(apps, schema_editor):
    Gastro = apps.get_model("data", "Gastro")
    Gastro.objects.all().update(is_submission=False)

    GastroSubmit = apps.get_model("data", "GastroSubmit")
    gastros_submit_old = GastroSubmit.objects.all().values()
    for gastro in gastros_submit_old:
        gastro.pop("id", None)
        gastro.pop("gastro_id", None)
        gastro_new = Gastro(**gastro)
        gastro_new.id_string = get_valid_id_string(Gastro)
        gastro_new.save()


class Migration(migrations.Migration):

    dependencies = [("data", "0009_gastro_add_is_submission")]

    operations = [
        migrations.RunPython(
            merge_gastro_gastro_submit, reverse_code=migrations.RunPython.noop
        )
    ]
