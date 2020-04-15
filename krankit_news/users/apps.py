from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "krankit_news.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import krankit_news.users.signals  # noqa F401
        except ImportError:
            pass
