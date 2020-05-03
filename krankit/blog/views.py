from django.views import generic
from krankit.blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "pages/home.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "pages/post_detail.html"
