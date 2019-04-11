from django.contrib.auth import get_user_model
from rest_framework import serializers
from musi_find_backend.models import Profile
from musi_find_backend.models import Instrument
from musi_find_backend.models import Genre
from musi_find_backend.models import Follow
from musi_find_backend.models import Publication
from musi_find_backend.models import Message
from musi_find_backend.models import Ban
from django.contrib.auth.models import User
import datetime

# Todo el rollo de autenticacion, sesiones y usuarios
class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name','email')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if len(Profile.objects.filter(profile_id=user.id)) == 0:
            first_instrument = Instrument.objects.first()
            first_genre = Genre.objects.first()
            new_profile = Profile(profile_id=user.id,instrument=first_instrument,genre=first_genre)
            new_profile.save()
        return user


# Actualizar profile
class ProfileSerializer(serializers.ModelSerializer):
    instrument = serializers.PrimaryKeyRelatedField(queryset=Instrument.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    class Meta:
        model = Profile #'profile_id',
        fields = ('description', 'mobile', 'email', 'facebook', 'twitter', 'instrument', 'genre','gender')


# Actualizar is_musician
class IsMusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('is_musician',)


# Cargar genero(s) 
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

# Cargar insturmento(s)
class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id','name',)


# Cargar datos de profile(s) para visualizacion (sin purblicaciones)
class ProfileViewerSerializer(serializers.ModelSerializer):
    instrument_name = serializers.SerializerMethodField()
    genre_name = serializers.SerializerMethodField()
    profile_name = serializers.SerializerMethodField()
    profile_username = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name','profile_name','profile_username','is_musician','gender')

    def get_instrument_name(self, obj):
        return obj.instrument.name

    def get_genre_name(self, obj):
        return obj.genre.name
    
    def get_profile_name(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        full_name = user.first_name + ' ' + user.last_name
        return full_name

    def get_profile_username(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        username = user.username
        return username

# Dar de alta follows
class FollowSerializer(serializers.ModelSerializer):
    followed_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    class Meta:
        model = Follow
        fields = ('followed_id',)


# Manejar publicaciones
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id','title','content',)


class FullProfileFlatSerializer(serializers.ModelSerializer):
    instrument_name = serializers.SerializerMethodField()
    genre_name = serializers.SerializerMethodField()
    profile_name = serializers.SerializerMethodField()
    profile_username = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name','profile_username','profile_name','is_musician','gender')

    def get_instrument_name(self, obj):
        return obj.instrument.name

    def get_genre_name(self, obj):
        return obj.genre.name

    def get_profile_name(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        full_name = user.first_name + ' ' + user.last_name
        return full_name

    def get_profile_username(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        username = user.username
        return username

# Manejar mensajes
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','sender_id','recipient_id','time_sent','content','seen')

    def create(self, validated_data):
        message = super(MessageSerializer, self).create(validated_data)
        message.sender_id = self.context.get('user_id')
        message.save()
        return message


# Mostrar perfiles con su rspectiva cantidad e mensajes no vistos con respecto al propio perfil
class ChatProfileFlatSerializer(serializers.ModelSerializer):
    profile_name = serializers.SerializerMethodField()
    profile_username = serializers.SerializerMethodField()
    count_of_unseen = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('profile_id','profile_username','profile_name','count_of_unseen')

    def get_profile_name(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        full_name = user.first_name + ' ' + user.last_name
        return full_name

    def get_profile_username(self, obj):
        user = User.objects.get(pk=obj.profile_id)
        username = user.username
        return username

    def get_count_of_unseen(self, obj):
        main_profile_id = self.context.get('user_id')
        other_id = obj.profile_id
        count_of_unseen = Message.objects.filter(recipient_id = main_profile_id).filter(sender_id=other_id).filter(seen=False).count()
        return count_of_unseen

# Generar registros de baneamento desde propio perfil a otro
class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = ('banned',)

    def create(self, validated_data):
        ban = super(BanSerializer, self).create(validated_data)
        ban.banner = self.context.get('user_id')
        ban.save()
        return ban
