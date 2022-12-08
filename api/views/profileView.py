from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.profile import Profile
from api.serializers.profileSerializers import ProfileSerializer


class ProfileModelViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]
    serializer_class = ProfileSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user=user.id)
        