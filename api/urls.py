from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet,CategoryViewSet,AuthorViewSet,MemberViewSet,BorrowViewSet,ReturnBookViewSet

from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('books',BookViewSet, basename='book-list')
router.register('categories', CategoryViewSet, basename='category-list')
router.register('authors', AuthorViewSet, basename='author-list')
router.register('members', MemberViewSet, basename='member-list')
router.register('borrow-book', BorrowViewSet, basename='borrow-book')
router.register('return-book', ReturnBookViewSet, basename='return-book')


book_router = routers.NestedDefaultRouter(router, 'books', lookup='books')
category_router = routers.NestedDefaultRouter(router, 'categories', lookup='categories')
author_router = routers.NestedDefaultRouter(router, 'authors', lookup='authors')
member_router = routers.NestedDefaultRouter(router, 'members', lookup='members')
borrow_router = routers.NestedDefaultRouter(router, 'borrow-book', lookup='borrow_book')
return_router = routers.NestedDefaultRouter(router, 'return-book', lookup='return_book')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
    path('', include(category_router.urls)),
    path('', include(author_router.urls)),
    path('', include(member_router.urls)),
    path('', include(borrow_router.urls)),
    path('', include(return_router.urls)),
]
