# Generated by Django 4.1.3 on 2022-11-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0006_remove_food_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="backend.foodcategory",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="food", name="type", field=models.IntegerField(default=0),
        ),
    ]
