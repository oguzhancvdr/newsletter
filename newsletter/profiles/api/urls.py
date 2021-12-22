from django.urls import path
from profiles.api.views import ProfileList

urlpatterns = [
  path('user_profiles/', ProfileList.as_view(), name="profiles" )
]