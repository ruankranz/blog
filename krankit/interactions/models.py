from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from krankit.utils.models import BaseModel


class Comment(BaseModel):
    content = models.TextField(max_length=5000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Vote(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes"
    )

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
