from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('like/<int:book_id>', views.like),
    path('<int:book_id>', views.book_info),
    path('<int:book_id>/update', views.update),
    path('<int:book_id>/delete', views.delete),
    path('logout', views.logout),
    path('add_like/<int:book_id>', views.add_like),
    path('unlike/<int:book_id>', views.unlike),
    path('my_books', views.my_books),
]

