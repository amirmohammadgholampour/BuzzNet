from django.contrib import admin
from django.utils.html import format_html
from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author_email",
        "short_text",
        "created_at",
        "updated_at",
        "likes_count",
        "image_preview",
        "video_preview",
    )
    list_filter = ("created_at", "author")
    search_fields = ("text", "author__email")
    readonly_fields = ("created_at", "updated_at", "image_preview", "video_preview")
    ordering = ("-created_at",)

    # Show author email
    def author_email(self, obj):
        return obj.author.email
    author_email.short_description = "Author"

    # Short text preview
    def short_text(self, obj):
        return (obj.text[:50] + "...") if obj.text else "—"
    short_text.short_description = "Text"

    # Count likes
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"

    # Show image preview
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:5px"/>', obj.image.url
            )
        return "—"
    image_preview.short_description = "Image"

    # Show video link
    def video_preview(self, obj):
        if obj.video:
            return format_html('<a href="{}" target="_blank">🎬 Video</a>', obj.video.url)
        return "—"
    video_preview.short_description = "Video"