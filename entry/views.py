from django.views.generic import ListView, DetailView

from models import Post


class PostListView(ListView):
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.get_visible()


class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.objects.get_visible()
