from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

from krankit.utils.models import BaseModel
from krankit.interactions.models import Comment

STATUS = ((0, "Draft"), (1, "Published"))


class Post(BaseModel):
    title = models.CharField(_("Title of post"), max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    published_on = models.DateTimeField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {"pk": self.id, "slug": self.slug}
        return reverse("article-pk-slug-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class PostComment(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
