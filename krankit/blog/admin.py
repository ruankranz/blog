from django.contrib import admin
from krankit.blog.models import Post, PostComment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("post__title", "content")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, CommentAdmin)
