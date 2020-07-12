from django.contrib import admin
from p_library.models import Book, Maker, BookMaker, Friend

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('avatar', 'title', 'author_full_name', 'price', 'friend_name')
    fields = ('avatar','ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher', 'friend_name')


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    @staticmethod
    def maker_name(obj):
        return obj.Maker.make_name

    list_display = ('make_name', 'make_country')
    fields = ('make_name', 'make_country' )

@admin.register(BookMaker)
class BookMakerAdmin(admin.ModelAdmin):
    @staticmethod
    def bookmaker_name(obj):
        return obj.BookMaker.publisher

    list_display = ('publisher', 'book', 'year')
    fields = ('publisher', 'book', 'year')

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    @staticmethod
    def friend_name(obj):
        return obj.Friend.friend_name

    list_display = ('friend_name', 'friend_book')
    fields = ('friend_name', 'friend_book')

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друг"