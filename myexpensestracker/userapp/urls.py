from django.urls import path
from .views import *


urlpatterns = [
    path('', BaseProfileView.as_view(), name='userprofile'),
    path('profilepage/', ProfilePage.as_view(), name='profilepage'),
    path('profileupdate', UserProfileUpdateView.as_view(), name='updateprofile'),
    
    # path('profile/update/', ProfileUpdateView.as_view(), name='profile-update')

]