from django.db import models
from django.utils.translation import gettext_lazy as _



class Article(models.Model):
    author = models.CharField(max_length=150, verbose_name=_('author'))
    headline = models.CharField(max_length=120, verbose_name=_('headline'))
    description = models.CharField(max_length=200, verbose_name=_('description'))
    content = models.TextField(verbose_name=_('content'))
    city = models.CharField(max_length=120, verbose_name=_('city'))
    pub_date = models.DateField(verbose_name=_(' published date'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('modified at'))

    class Meta:
      verbose_name = _("article")
      verbose_name_plural = _("articles")

    def __str__(self):
      return self.headline
