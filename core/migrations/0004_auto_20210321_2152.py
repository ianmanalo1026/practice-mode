# Generated by Django 3.1.4 on 2021-03-21 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210321_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='course',
            new_name='subject',
        ),
    ]