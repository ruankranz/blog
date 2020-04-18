from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PollsConfig(AppConfig):
    name = "krankit.polls"
    verbose_name = _("Polls")

    def ready(self):
        try:
            import krankit.polls.signals  # noqa F401
        except ImportError:
            pass
