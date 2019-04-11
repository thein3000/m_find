# Generated by Django 2.1.7 on 2019-04-11 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.IntegerField(blank=True, null=True, verbose_name='Baneador')),
                ('banned', models.IntegerField(blank=True, null=True, verbose_name='Baneado')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.IntegerField(blank=True, null=True, verbose_name='Seguidor')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField(blank=True, null=True, verbose_name='Emisor')),
                ('recipient_id', models.IntegerField(blank=True, null=True, verbose_name='Receptor')),
                ('time_sent', models.DateTimeField(auto_now_add=True, verbose_name='Fecha hora de envio')),
                ('content', models.CharField(max_length=500, verbose_name='Contenido')),
                ('seen', models.BooleanField(default=False, verbose_name='Visto')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('is_musician', models.BooleanField(default=False, verbose_name='Músico')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Descripción')),
                ('mobile', models.CharField(blank=True, max_length=20, verbose_name='Móvil/Whatsapp')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Correo')),
                ('facebook', models.CharField(blank=True, max_length=30, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=30, verbose_name='Twitter')),
                ('gender', models.CharField(blank=True, default='Masculino', max_length=10, verbose_name='Sexo')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='musi_find_backend.Genre', verbose_name='Genero principal')),
                ('instrument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='musi_find_backend.Instrument', verbose_name='Instrumento principal')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Título')),
                ('content', models.CharField(max_length=300, verbose_name='Contenido')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musi_find_backend.Profile', verbose_name='Publicante')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rater', models.IntegerField(verbose_name='Calificante')),
                ('score', models.FloatField()),
                ('rated', models.ForeignKey(on_delete='Calificador', to='musi_find_backend.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='followed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musi_find_backend.Profile', verbose_name='Seguido'),
        ),
    ]
