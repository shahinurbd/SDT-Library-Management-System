from rest_framework import serializers
from books.models import Book,Category,Author,BorrowRecord,ReturnBook
from users.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'category', 'availability']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'membership_date']


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'borrow_date', 'return_date']

    def validate(self, data):
        book = data.get('book')
        if not book.availability:
            raise serializers.ValidationError({"error": "This book is already borrowed."})
        return data
    


class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnBook
        fields = ['id', 'book', 'return_date', 'fine_amount', 'book_condition']


    def validate(self, data):
        book = data.get("book")
        if book.availability:
            raise serializers.ValidationError({"error": "This book is not borrowed."})
        return data


    
