from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from krankit.utils.models import BaseModel
from krankit.interactions.models import Vote


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    asked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Choice(BaseModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_text = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class ChoiceVote(Vote):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes")
