from django.contrib.syndication.views import Feed

from models import Post


class LatestPostsFeed(Feed):
    title = "Nyarlathotep News"
    link = '/'
    description = "Updates on changes and additions"

    def items(self):
        return Post.objects.get_visible().order_by('-publish_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

#    def link(self, item):
#        return item.get_absolute_url()
