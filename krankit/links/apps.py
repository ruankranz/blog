from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinksConfig(AppConfig):
    name = "krankit.links"
    verbose_name = _("Links")

    def ready(self):
        try:
            import krankit.links.signals  # noqa F401
        except ImportError:
            pass
