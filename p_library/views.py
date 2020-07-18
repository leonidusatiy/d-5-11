from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from p_library.models import Book, Publisher, Author, Friend
from p_library.forms import AuthorForm, FriendForm


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorEdit(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'


class FriendEdit(UpdateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


def friend_delete(request, pk):
    if request.method == 'POST':
        if not pk:
            return redirect(reverse_lazy('p_library:friend_list'))
        else:
            friend = Friend.objects.filter(id=pk).first()
            if not friend:
                return redirect(reverse_lazy('p_library:friend_list'))
            friend.delete()
            return redirect(reverse_lazy('p_library:friend_list'))
    else:
        return redirect(reverse_lazy('p_library:friend_list'))


def index(request):
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку",
                   "books": books}
    return render(request, 'index.html', biblio_data)


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect(reverse_lazy('main'))
            book.copy_count += 1
            book.save()
        return redirect(reverse_lazy('main'))
    else:
        return redirect(reverse_lazy('main'))


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect(reverse_lazy('main'))
    else:
        return redirect(reverse_lazy('main'))


def publishers(request):
    publishers_data = {"publishers": Publisher.objects.order_by('title')}
    return render(request, 'publishers.html', publishers_data)


