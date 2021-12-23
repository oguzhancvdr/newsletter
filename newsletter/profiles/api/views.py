from rest_framework import generics, serializers, mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet
from profiles.api.permissions import IsProfileOwnerOrReadOnly, IsStatusOwnerOrReadOnly
from rest_framework.filters import SearchFilter


class ProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]
    filter_backends = [SearchFilter,]
    search_fields = ['city',]


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsStatusOwnerOrReadOnly]

    def get_queryset(self):
        # burda ProfileStatus modeli üzerinde çalışıyoruz
        # dolayısıyla filtrelemeyi user_profil üzerinden yapıyoruz username'e ulaşmak için
        # bu user_profile bağlı Profil model'inde ki user'a ulaşıyoruz ve buna bağlı username'i çekiyoruz
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

# tek bir instance(profil) nesnesi üzerinde çalışcağımız için
# burda ModelViewSet kullanmamıza gerek yok


class ProfileAvatarUpdateView(generics.UpdateAPIView):
    # burda queryset'e ihtiyaç yok
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated, ]

    # queryseti override ettik
    # gerekli değişiklipi yaptık ve gerisini UpdateAPIView'e braktık
    # permission'ı requestten user'ın kendi profilini aldığımız için
    # IsAuthenticated bize burda yeterli oldu
    def get_object(self):
        profile_obj = self.request.user.profile
        return profile_obj
