from rest_framework import generics, serializers, mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from profiles.api.permissions import IsProfileOwnerOrReadOnly


class ProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]
