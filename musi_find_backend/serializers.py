from django.contrib.auth import get_user_model
from rest_framework import serializers
from musi_find_backend.models import Profile
from musi_find_backend.models import Instrument
from musi_find_backend.models import Genre
from musi_find_backend.models import Follow
from musi_find_backend.models import Publication

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
        new_profile = Profile(profile_id=user.id)
        new_profile.save()
        return user


# Actualizar profile
class ProfileSerializer(serializers.ModelSerializer):
    instrument = serializers.PrimaryKeyRelatedField(queryset=Instrument.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    class Meta:
        model = Profile #'profile_id',
        fields = ('description','mobile','email','facebook','twitter','instrument','genre')


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
    class Meta:
        model = Profile
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name')

    def get_instrument_name(self, obj):
        return obj.instrument.name

    def get_genre_name(self, obj):
        return obj.genre.name


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
        fields = ('title','content',)


class FullProfileFlatSerializer(serializers.ModelSerializer):
    instrument_name = serializers.SerializerMethodField()
    genre_name = serializers.SerializerMethodField()
    # publication = PublicationSerializer(source='Publication', many=True)
    class Meta:
        model = Profile
        fields = ('profile_id','description','mobile','email','facebook','twitter','instrument_name','genre_name',)#'publication',)

    def get_instrument_name(self, obj):
        return obj.instrument.name

    def get_genre_name(self, obj):
        return obj.genre.name
