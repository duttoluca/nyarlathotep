from django.contrib import admin

from entry.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('active', 'title', 'created', 'modified', 'publish_at', 'author',)
    list_display_links = ('title', 'author',)
    list_editable = ('active',)
    list_filter = ('modified', 'created', 'active', "publish_at")
    date_hierarchy = "publish_at"
    search_fields = ["title", "body",
                     "author"]
    fieldsets = (
                (None, {
                        'fields': ('title', 'categories',)}
                 ),
                 ('Publication', {"fields": ("active", "publish_at"),
                                  "description": "Controlla se e quando il post e' visibile."}
                  ),
                 ("Content", {"fields": ("body",)}
                  ),
                 ('Optional', {"fields": ("slug",),
                               "classes": ("collapse",)})
    )

    # questo save permette di salvare automaticamente l'utente loggato come autore
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'active',)
    list_display_links = ('name',)
    list_editable = ('active',)
    search_fields = ['name']
    fieldsets = (
                (None, {
                        'fields': ('name', 'active',)}
                 ),
                 ('Optional', {"fields": ("slug",),
                               "classes": ("collapse",)})
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
