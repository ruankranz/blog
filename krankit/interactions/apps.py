from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InteractionsConfig(AppConfig):
    name = "krankit.interactions"
    verbose_name = _("Interactions")

    def ready(self):
        try:
            import krankit.interactions.signals  # noqa F401
        except ImportError:
            pass
