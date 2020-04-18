from django.contrib import admin
from krankit.blog.models import Post, PostComment

admin.site.register(Post)
admin.site.register(PostComment)
