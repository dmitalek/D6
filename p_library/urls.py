from django.urls import path
from .views import AuthorEdit, AuthorList, BookEdit, FriendList, FriendUpdate, FriendEdit, author_create_many


app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('book/create', BookEdit.as_view(), name='book_create'),
    path('friends', FriendList.as_view(), name='friend_list'),
    path('<pk>/friend_update', FriendUpdate.as_view(), name='friend_update'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('author/create_many', author_create_many, name='author_create_many'), 
]