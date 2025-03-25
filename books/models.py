from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField()

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author'
    )
    isbn = models.CharField(max_length=20)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class BorrowRecord(models.Model):
    book = models.ForeignKey(
        Book, related_name='book',on_delete=models.CASCADE)
    member = models.ForeignKey(
        Member,on_delete=models.CASCADE,default=1, related_name='member'
    )
    borrow_date = models.DateField()
    return_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.book.availability:
            raise ValueError("This book is already borrowed.")
        self.book.availability = False
        self.book.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.book.availability = True
        self.book.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.book
    

class ReturnBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateField(auto_now_add=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    condition_choices = [
        ('good', 'Good'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
    ]
    book_condition = models.CharField(max_length=10, choices=condition_choices, default='good')

    def save(self, *args, **kwargs):
        self.book.availability = True
        self.book.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.book.title} has been returned on {self.return_date}"
