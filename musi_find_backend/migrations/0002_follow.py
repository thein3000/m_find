# Generated by Django 2.1.7 on 2019-04-03 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musi_find_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.IntegerField(verbose_name='Seguidor')),
                ('followed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musi_find_backend.Profile', verbose_name='Seguido')),
            ],
        ),
    ]