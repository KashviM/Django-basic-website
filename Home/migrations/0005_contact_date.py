# Generated by Django 4.0.4 on 2022-05-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_remove_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=20220527),
            preserve_default=False,
        ),
    ]
