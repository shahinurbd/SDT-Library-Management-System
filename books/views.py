from django.shortcuts import render
from rest_framework.response import Response
from books import serializers
from books.models import Book,Category,Author,Member,BorrowRecord,ReturnBook
from books.serializers import BookSerializer,CategorySerializer,AuthorSerializer,MemberSerializer,BorrowRecordSerializer,ReturnBookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.availability:
            raise serializers.ValidationError({"error": "This book is already borrowed."})
        serializer.save()

class ReturnBookViewSet(ModelViewSet):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.availability:
            return Response({"error": "This book is not borrowed."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        