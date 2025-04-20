from django.shortcuts import render
from rest_framework.response import Response
from books import serializers
from books.models import Book,Category,Author,BorrowRecord,ReturnBook
from users.models import User
from books.serializers import BookSerializer,CategorySerializer,AuthorSerializer,MemberSerializer,BorrowRecordSerializer,ReturnBookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class MemberViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]

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
        