from django.shortcuts import redirect, render
from django.apps import apps
User = apps.get_model('login_app', 'User')
from .models import *
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
        'user': User.objects.get(id =request.session['user_id']),
        'books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def add(request):
    this_user= User.objects.get(id = request.session['user_id'])
    errors= Book.objects.book_validator(request.POST)
    request.session['send']= 'add_book'
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/books')
    else:
        this_book= Book.objects.create(title= request.POST['title'], desc= request.POST['desc'], uploaded_by= this_user)
        this_book.liked_by.add(this_user)
        request.session['book_id']= this_book.id
        return redirect('/books')

def like(request, book_id):
    this_user= User.objects.get(id = request.session['user_id'])
    this_book= Book.objects.get(id= book_id)
    this_book.liked_by.add(this_user)
    return redirect('/books')

def book_info(request, book_id):
    this_book= Book.objects.get(id= book_id)
    if this_book.uploaded_by.id == request.session['user_id']:        
        context={
            'book': Book.objects.get(id= book_id),
            'user': User.objects.get(id= request.session['user_id']),
    }
        return render(request, 'book_info.html', context)
    else:
        context={
            'book': Book.objects.get(id= book_id),
            'user': User.objects.get(id= request.session['user_id']),
    }
        return render(request, 'book_inform.html', context)

def update(request, book_id):
    request.session['send']= 'update_book'
    errors= Book.objects.update_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/books/{book_id}')
    this_book= Book.objects.get(id=book_id)
    this_book.title= request.POST['title']
    this_book.save()
    this_book.desc = request.POST['desc']
    this_book.save()
    return redirect(f'/books/{book_id}')

def delete(request, book_id):
    this_book= Book.objects.get(id= book_id)
    this_book.delete()
    return redirect('/books')

def add_like(request, book_id):
    this_user= User.objects.get(id = request.session['user_id'])
    this_book= Book.objects.get(id= book_id)
    this_book.liked_by.add(this_user)
    return redirect(f"/books/{book_id}")

def unlike(request, book_id):
    this_user= User.objects.get(id = request.session['user_id'])
    this_book= Book.objects.get(id= book_id)
    this_book.liked_by.remove(this_user)
    return redirect(f"/books/{book_id}")

def my_books(request):
    context={
        'user': User.objects.get(id= request.session['user_id'])
    }
    return render(request, 'my_books.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')