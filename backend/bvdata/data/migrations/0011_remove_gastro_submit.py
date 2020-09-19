from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("data", "0010_merge_gastro_gastro_submit")]

    operations = [
        migrations.RemoveField(model_name="gastrosubmit", name="gastro"),
        migrations.DeleteModel(name="GastroSubmit"),
    ]
