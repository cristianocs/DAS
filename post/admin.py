from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['autor','titulo']
    list_filter = ['autor']
    search_fields = ['autor', 'titulo']
    save_on_top = True
admin.site.register(Post, PostAdmin)