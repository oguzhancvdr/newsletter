from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Book(models.Model):
  name = models.CharField(max_length=255, verbose_name=_('Name'))
  author = models.CharField(max_length=255, verbose_name=_('Author'))
  description = models.CharField(max_length=255, verbose_name=_('Description'), blank=True)
  published_at = models.DateTimeField(verbose_name=_('Published date'))
  created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated date'))

  def __str__(self):
    return f"{self.name}-{self.author}"


class Comment(models.Model):
  book = models.ForeignKey(Book, verbose_name=_('Book'), on_delete=models.CASCADE, related_name='comments')
  # owner = models.CharField(max_length=255, verbose_name=_('Owner'))
  owner = models.ForeignKey(User, max_length=255, verbose_name=_('Owner'), on_delete=models.CASCADE)
  comment = models.TextField(blank=True, null=True, verbose_name=_('Comment'))
  rating = models.PositiveBigIntegerField(verbose_name=_('Rating'),
    validators=[MinValueValidator(1), MaxValueValidator(5)]
  )
  created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated date'))

  def __str__(self):
    return f"{self.owner}-{str(self.rating)}"
