from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    name = "krankit.blog"
    verbose_name = _("Blog")

    def ready(self):
        try:
            import krankit.blog.signals  # noqa F401
        except ImportError:
            pass
