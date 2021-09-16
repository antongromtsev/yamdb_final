from django.contrib import admin

from .models.categories import Category
from .models.comments import Comments
from .models.genres import Genre
from .models.review import Review
from .models.titles import Title
from .models.users import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "bio", "username", "role")
    search_fields = ("role",)
    list_filter = ("username",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


class TitleAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description")
    search_fields = ("description",)
    list_filter = ("year",)
    empty_value_display = "-пусто-"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("review", "text", "author", "pub_date")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("slug",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author", "score", "pub_date")
    search_fields = ("author",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
