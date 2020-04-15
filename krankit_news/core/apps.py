from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "krankit_news.core"
    verbose_name = _("Core")

    def ready(self):
        try:
            import krankit_news.core.signals  # noqa F401
        except ImportError:
            pass
