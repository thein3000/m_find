from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView
# from .views import ProfileInstruments
from .views import HandleProfile, RetrieveGenres, RetrieveInstruments, ListFlatProfiles, UpdateIsMusician
from .views import AddFollow, HandlePublication, ListFollowedProfiles, FullProfile

urlpatterns = [
    url('auth/login/', obtain_auth_token, name='auth_user_login'),
    url('auth/register/', CreateUserAPIView.as_view(), name='auth_user_create'),
    url('auth/logout/', LogoutUserAPIView.as_view(), name='auth_user_logout'),
    url('profile/handle_profile/', HandleProfile.as_view(), name='handle_profile'),
    url('profile/update_is_musician/', UpdateIsMusician.as_view(), name='update_is_musician'),
    url('profile/list_flat_profiles/', ListFlatProfiles.as_view(), name='list_flat_profiles'),
    url('profile/list_followed_profiles/', ListFollowedProfiles.as_view(), name='list_followed_profiles'),
    url('profile/full_profile/', FullProfile.as_view(), name='full_profile'),
    url('follow/add_follow/', AddFollow.as_view(), name='add_follow'),
    url('publication/handle_publication/', HandlePublication.as_view(), name='handle_publication'),
    url('retrieve_instruments/', RetrieveInstruments.as_view(), name='retrieve_instruments'),
    url('retrieve_genres/', RetrieveGenres.as_view(), name='retrieve_genres'),
]