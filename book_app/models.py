from django.db.models.deletion import CASCADE
from django.db import models

class BookManager(models.Manager):
    def book_validator(self, post_data):
        errors= {}
        if len(post_data['title']) < 1:
            errors['title_input']= "Title is required."
        if len(post_data['desc']) < 5:
            errors['des_input']= "Description must be at least 5 characters long."
        return errors

    def update_validator(self, post_data):
        errors= {}
        if len(post_data['new_title']) < 1:
            errors['title_update']= "Title is required."
        if len(post_data['new_desc']) < 5:
            errors['des_update']= "Description must be at least 5 characters long."
        return errors


# books_uploaded = a list of books uploaded by a given user
# liked_books = a list of books a given user likes


class Book(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField()
    uploaded_by= models.ForeignKey('login_app.User', related_name='books_uploaded', on_delete=CASCADE)
    liked_by= models.ManyToManyField('login_app.User', related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= BookManager()


