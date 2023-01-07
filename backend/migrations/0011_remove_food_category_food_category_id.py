# Generated by Django 4.1.3 on 2022-11-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0010_remove_foodcategory_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="food", name="category",),
        migrations.AddField(
            model_name="food",
            name="category_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
