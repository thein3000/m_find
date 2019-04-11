from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView
from .views import HandleProfile, RetrieveGenres, RetrieveInstruments, ListFlatProfiles, UpdateIsMusician
from .views import AddFollow, HandlePublication, ListFollowedProfiles, FullProfile, OwnFullProfile
from .views import ChatMessages, NumberOfNewMessages, ChatProfiles, MarkMessagesAsSeen, BanProfile

urlpatterns = [
    url('auth/login/', obtain_auth_token, name='auth_user_login'),
    url('auth/register/', CreateUserAPIView.as_view(), name='auth_user_create'),
    url('auth/logout/', LogoutUserAPIView.as_view(), name='auth_user_logout'),
    url('profile/handle_profile/', HandleProfile.as_view(), name='handle_profile'),
    url('profile/update_is_musician/', UpdateIsMusician.as_view(), name='update_is_musician'),
    url('profile/list_flat_profiles/', ListFlatProfiles.as_view(), name='list_flat_profiles'),
    url('profile/list_followed_profiles/', ListFollowedProfiles.as_view(), name='list_followed_profiles'),
    url('profile/full_profile/', FullProfile.as_view(), name='full_profile'),
    url('profile/own_full_profile/', OwnFullProfile.as_view(), name='own_full_profile'),    
    url('follow/add_follow/', AddFollow.as_view(), name='add_follow'),
    url('publication/handle_publication/', HandlePublication.as_view(), name='handle_publication'),
    url('retrieve_instruments/', RetrieveInstruments.as_view(), name='retrieve_instruments'),
    url('retrieve_genres/', RetrieveGenres.as_view(), name='retrieve_genres'),
    url('messages/chat_messages/', ChatMessages.as_view(), name='chat_messages'),
    url('messages/number_of_new_messages/', NumberOfNewMessages.as_view(), name='number_of_new_messages'),
    url('messages/chat_profiles/', ChatProfiles.as_view(), name='chat_profiles'),
    url('messages/mark_messages_as_seen/', MarkMessagesAsSeen.as_view(), name='mark_messages_as_seen'),
    url('ban/ban_profile/', BanProfile.as_view(), name='ban_profile'),
]