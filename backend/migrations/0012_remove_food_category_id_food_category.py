# Generated by Django 4.1.3 on 2022-11-07 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0011_remove_food_category_food_category_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="food", name="category_id",),
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
    ]