from django.db import models


class Instrument(models.Model):
    name = models.CharField("Nombre", max_length=30)


class Genre(models.Model):
    name = models.CharField("Nombre", max_length=30)


class Profile(models.Model):
    profile_id = models.IntegerField("Id", primary_key=True)
    is_musician = models.BooleanField("Músico", default=False)
    description = models.CharField("Descripción", max_length=300, blank=True)
    mobile = models.CharField("Móvil/Whatsapp", max_length=20, blank=True)
    email = models.CharField("Correo", max_length=30, blank=True)
    facebook = models.CharField("Facebook", max_length=30, blank=True)
    twitter = models.CharField("Twitter", max_length=30, blank=True)
    instrument = models.ForeignKey(Instrument, verbose_name="Instrumento principal", null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, verbose_name="Genero principal", null=True, blank=True,on_delete=models.SET_NULL)


class Publication(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="Publicante",null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=30)
    content = models.CharField("Contenido", max_length=300)
    publish_date = models.DateField("Fecha",null=True, blank=True,)


class Rating(models.Model):
    rated = models.ForeignKey(Profile, "Calificador")
    rater = models.IntegerField("Calificante")
    score = models.FloatField()


class Follow(models.Model):
    follower_id = models.IntegerField("Seguidor", blank=True, null=True)
    followed_id = models.ForeignKey(Profile, verbose_name="Seguido",on_delete=models.CASCADE)
    