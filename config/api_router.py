from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from krankit.users.api.views import UserViewSet
from krankit.blog.api.views import PostViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("posts", PostViewSet)


app_name = "api"
urlpatterns = router.urls
