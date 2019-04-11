from django.contrib.auth import get_user_model
from rest_framework import serializers
from musi_find_backend.models import Profile
from musi_find_backend.models import Instrument
from musi_find_backend.models import Genre
from musi_find_backend.models import Follow
from musi_find_backend.models import Publication
from django.contrib.auth.models import User

# Todo el rollo de autenticacion, sesiones y usuarios
class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
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
        fields = ('description', 'mobile', 'email', 'facebook', 'twitter', 'instrument', 'genre')


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
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name','profile_name','profile_username','is_musician')

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
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name','profile_username','profile_name','is_musician')

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