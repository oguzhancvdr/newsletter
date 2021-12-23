from django.urls import path
from django.urls.conf import include
from django.views.generic import base
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, ProfileAvatarUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet, basename='status')


# before router implementation
# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
  # path('user_profiles/', profile_list, name="profiles" ),
  # path('user_profiles/<int:pk>',profile_detail, name="profile_detail" ),
  path('', include(router.urls)),
  # viewset olmadığı için clasic path yazmalıız
  path('profile_avatar/', ProfileAvatarUpdateView.as_view(), name="profile-avatar"),
]