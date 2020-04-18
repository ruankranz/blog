from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from krankit.utils.models import BaseModel
from krankit.interactions.models import Vote


class Link(BaseModel):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="links",
    )

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class LinkVote(Vote):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="votes")
