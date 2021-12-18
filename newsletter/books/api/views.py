from rest_framework import generics
# çekilen obje varsa al yoksa 404 döndürmek için alıyoruz
from rest_framework.generics import get_object_or_404
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from books.models import Book, Comment
from books.api.serializers import BookSerializer, CommentSerializer
from books.api.permissions import IsAdminUserOrReadOnly, IsCommentOwnerOrReadOnly


class BookListCreateAPIView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAdminUserOrReadOnly]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAdminUserOrReadOnly]

class CommentCreateAPIView(generics.CreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    # burda url'den gelecek olan pk ya da id'yi get ile çektik.
    # burda yorum modelimizle foreign key olan kitabı bir şekilde dahil etmeliyiz
    # çünkü hangi kitaba yorum yapılacağı belli olmalı
    # bundan dolayı oluşturduğumuz url pathin'den
    # path('books/<int:book_pk>/comment',api_views.CommentCreateAPIView.as_view(), name="create-comment"),
    # book_pk'yi yakalayıp, get_object_or_404 methoduna göndererek
    # varsa o kitaba yorum yapacak enpointe yoksa 404 dönmesini sağlıyoruz
    # burda ki sorun oluşturdğumuz url'e gidildiğinde book fieldi olduğu için
    # diğer eklenmiş kitaplarda görünüyordu ama biz burda serializera giderek 
    # book alanını exclude edip kullanıcıya seçim şansını tanımıyoruz
    book_pk = self.kwargs.get('book_pk')
    book = get_object_or_404(Book, pk=book_pk)

    # current user drf bizim için request'ten gönderiyor
    current_user = self.request.user

    # bir kullanıcı her kitaba yalnızca bir kez yorum yapabilir
    comments = Comment.objects.filter(book=book, owner=current_user)
    if comments.exists():
      raise ValidationError('You can comment just one time for any book.')

    # burdaki owner serializer modelden alıp view'e taşıyor
    serializer.save(book=book, owner=current_user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [IsCommentOwnerOrReadOnly]

  








# ? with mixins
"""
class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
  # todo: 1. listelemek
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  # todo: 2. Kitap oluşturmak
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
"""