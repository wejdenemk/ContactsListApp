# Generated by Django 4.1.4 on 2022-12-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_fav_contact_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='favourite',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
