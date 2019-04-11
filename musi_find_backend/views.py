from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from musi_find_backend.serializers import CreateUserSerializer
from rest_framework import authentication, permissions
from musi_find_backend.models import Profile, Instrument, Genre, Follow, Publication, Message, Ban
from musi_find_backend.serializers import ProfileSerializer
from musi_find_backend.serializers import InstrumentSerializer
from musi_find_backend.serializers import GenreSerializer
from musi_find_backend.serializers import ProfileViewerSerializer
from musi_find_backend.serializers import IsMusicianSerializer 
from musi_find_backend.serializers import FollowSerializer
from musi_find_backend.serializers import PublicationSerializer
from musi_find_backend.serializers import FullProfileFlatSerializer
from musi_find_backend.serializers import MessageSerializer
from musi_find_backend.serializers import ChatProfileFlatSerializer
from musi_find_backend.serializers import BanSerializer
import datetime

class RetrieveInstruments(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    def get(self, request, format=None):
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)


class RetrieveGenres(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class UpdateIsMusician(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profile = Profile.objects.get(pk=request.user.id)
        serializer = IsMusicianSerializer(profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        profile = Profile.objects.get(pk=request.user.id)
        serializer = IsMusicianSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HandleProfile(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profile = Profile.objects.get(pk=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        # profile_id = request.data.get('profile_id', None)
        # profile = Profile.objects.get(pk=int(profile_id))
        profile = Profile.objects.get(pk=request.user.id)
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddFollow(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    def get(self, request, format=None):
        followed_id = int(self.request.query_params.get('profile_id', None))
        follow = Follow.objects.filter(follower_id = request.user.id).filter(followed_id=followed_id)
        if len(follow) >= 1:
            is_followed = True
        else:
            is_followed = False
        return Response({"is_followed":is_followed})    


    def post(self, request, format=None):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            followed_id = request.data.get('followed_id', None)
            current_same_follows = Follow.objects.filter(follower_id = request.user.id).filter(followed_id=followed_id) 
            if len(current_same_follows) > 1:
                current_same_follows.delete()
            if len(current_same_follows) == 0:
                serializer.save()
                created_follow = Follow.objects.last()
                created_follow.follower_id = request.user.id
                created_follow.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HandlePublication(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profile_id = int(self.request.query_params.get('profile_id', None))
        publications = Publication.objects.filter(profile=profile_id)
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)    

    def post(self, request, format=None):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            created_publication = Publication.objects.last()
            created_publication.profile = Profile.objects.get(pk=request.user.id)
            created_publication.publish_date = datetime.datetime.now()
            created_publication.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListFlatProfiles(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profiles = Profile.objects.all().exclude(profile_id = request.user.id).filter(is_musician=True)
        serializer = ProfileViewerSerializer(profiles, many=True)
        return Response(serializer.data)


class FullProfile(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profile_id = int(self.request.query_params.get('profile_id', None))
        profile = Profile.objects.get(pk=profile_id)
        serializer = FullProfileFlatSerializer(profile)
        return Response(serializer.data)


class OwnFullProfile(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        profile_id = request.user.id
        profile = Profile.objects.get(pk=profile_id)
        serializer = FullProfileFlatSerializer(profile)
        return Response(serializer.data)


class ListFollowedProfiles(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        followed_list = Follow.objects.filter(follower_id = request.user.id).values_list('followed_id', flat=True)
        profiles = Profile.objects.filter(pk__in=followed_list).filter(is_musician=True)
        serializer = ProfileViewerSerializer(profiles, many=True)
        return Response(serializer.data)

class ChatMessages(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        main_user_id = request.user.id
        other_user_id = int(self.request.query_params.get('other_id', None))
        involved_users = [main_user_id, other_user_id]
        chat_messages = Message.objects.filter(sender_id__in = involved_users).filter(recipient_id__in = involved_users)
        serializer = MessageSerializer(chat_messages, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        context = {'user_id': request.user.id}
        serializer = MessageSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkMessagesAsSeen(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self,request, format=None):
        other_id = int(request.data.get('other_id'))
        profile = Profile.objects.filter(pk=other_id)
        if profile.count() >= 1:
            unseen_messages = Message.objects.filter(sender_id = other_id).filter(recipient_id = request.user.id).filter(seen=False)
            unseen_messages.update(seen=True)
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)

class NumberOfNewMessages(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        ban_list =  Ban.objects.filter(banner=request.user.id).values_list('banned',flat=True)
        number_of_messages = Message.objects.filter(recipient_id = request.user.id).filter(seen = False).exclude(sender_id__in=ban_list).count()
        return Response({"message_count": number_of_messages})


class ChatProfiles(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        context = {'user_id': request.user.id}
        main_user_id = request.user.id
        profiles_one_has_sent_to = list(Message.objects.filter(sender_id = main_user_id).values_list('recipient_id', flat=True))
        profile_that_have_sent_to_one = list(Message.objects.filter(recipient_id = main_user_id).values_list('sender_id', flat=True))
        profiles_with_chat = profiles_one_has_sent_to + profile_that_have_sent_to_one
        print(profiles_with_chat)
        ban_list =  Ban.objects.filter(banner=main_user_id).values_list('banned',flat=True)
        profiles = Profile.objects.filter(pk__in=profiles_with_chat).exclude(pk__in=ban_list).exclude(pk=main_user_id)
        serializer = ChatProfileFlatSerializer(profiles, many=True, context=context)
        return Response(serializer.data)

class BanProfile(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request, format=None):
        context = {'user_id': request.user.id}
        serializer = BanSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        token = Token.objects.create(user=serializer.instance)
        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



