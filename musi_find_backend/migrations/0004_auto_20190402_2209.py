# Generated by Django 2.1.7 on 2019-04-03 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musi_find_backend', '0003_auto_20190402_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='profile_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musi_find_backend.Profile', verbose_name='Publicante'),
        ),
    ]
