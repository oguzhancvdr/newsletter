from rest_framework import serializers
from books.models import Book, Comment



class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  # Burda many=True dememizin sebebi buraya 1den fazla yorum gelebilir
  # hazırlıklı ol diyoruz, read_only=True ise
  # ben kitap oluşturcam benden foreign key ile bağlı olan bu yorum tablosunu
  # zorunlu kılma ben direk kitabımı oluşturayım
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Book
    fields = '__all__'





# Kitaplar içinde yorumları göstermek istiyoruz
"""
{
  'name': 'First Book',
  'comments': [
    {"...."},
    {"...."},
  ],
}
"""