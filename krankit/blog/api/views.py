from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import PostSerializer
from krankit.blog.models import Post


class PostViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
