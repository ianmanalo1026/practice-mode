# Generated by Django 3.1.4 on 2021-03-21 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
    ]