from django.contrib import admin
from .models import Liveblog, Post

class PostAdmin(admin.ModelAdmin):

    list_display=["id", "liveblog", "created", "body_intro"]
    ordering=["-id"]

    def log_deletion(self, request, object, object_repr):
        object.delete_notification()
        super(PostAdmin, self).log_deletion(request, object, object_repr)



admin.site.register(
    Liveblog,
    list_display=["id", "title", "slug"],
    list_display_links=["id", "title"],
    ordering=["title"],
    prepopulated_fields={"slug": ("title",)},
)


admin.site.register(
    Post,PostAdmin
)
