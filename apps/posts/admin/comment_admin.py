from django.contrib import admin
from django.utils.html import format_html
from apps.posts.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "post_id_display",
        "author_email",
        "short_text",
        "created_at",
    )
    list_filter = ("created_at", "author", "post")
    search_fields = ("text", "author__email", "post__id")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    # Show related post ID (and link to post in admin)
    def post_id_display(self, obj):
        return format_html(
            '<a href="/admin/app_name/post/{}/change/">{}</a>',
            obj.post.id,
            obj.post.id,
        )
    post_id_display.short_description = "Post"

    # Show author email
    def author_email(self, obj):
        return obj.author.email
    author_email.short_description = "Author"

    # Shorten text for preview
    def short_text(self, obj):
        return (obj.text[:50] + "...") if obj.text else "—"
    short_text.short_description = "Text"
