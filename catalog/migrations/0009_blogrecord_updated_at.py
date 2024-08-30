# Generated by Django 5.0.7 on 2024-08-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_alter_blogrecord_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogrecord",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата последнего изменения"
            ),
        ),
    ]
