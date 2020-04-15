from django.db import models
from django.utils.translation import gettext_lazy as _
from krankit_news.users.models import User
from krankit_news.utils.models import BaseModel

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class Post(BaseModel):
    title = models.CharField(_("Title of post"), max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Comment(BaseModel):
    content = models.TextField(max_length=1500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})