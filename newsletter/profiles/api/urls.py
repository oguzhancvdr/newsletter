from django.urls import path
from django.urls.conf import include
from profiles.api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_profiles', ProfileViewSet)

# before router implementation
# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
  # path('user_profiles/', profile_list, name="profiles" ),
  # path('user_profiles/<int:pk>',profile_detail, name="profile_detail" ),
  path('', include(router.urls)),
]