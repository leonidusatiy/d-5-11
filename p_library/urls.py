from django.urls import path
from .views import AuthorCreate, AuthorList, AuthorEdit, FriendList, FriendCreate, FriendEdit, book_decrement, book_increment, publishers, index, friend_delete

app_name = 'p_library'

urlpatterns = [
    path('', index, name='main'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorEdit.as_view(), name='author_edit'),
    path('friend/create/', FriendCreate.as_view(), name='friend_create'),
    path('friend/', FriendList.as_view(), name='friend_list'),
    path('friend/<int:pk>/', FriendEdit.as_view(), name='friend_edit'),
    path('friend/<int:pk>/delete/', friend_delete, name='friend_delete'),
    path('book_increment/', book_increment),
    path('book_decrement/', book_decrement),
    path('publishers/', publishers, name='publishers'),
]