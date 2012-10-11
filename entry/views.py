from django.views.generic import ListView, DetailView

from models import Post, Category


class PostListView(ListView):
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.get_visible()


class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.objects.get_visible()


class PostListByCategoryView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.get_visible().filter(categories__slug__exact=slug)


class CategoryListView(ListView):
    def get_queryset(self):
        return Category.objects.filter(active=True)
