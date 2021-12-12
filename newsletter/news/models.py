from django.db import models
from django.utils.translation import gettext_lazy as _


class Reporter(models.Model):
    first_name = models.CharField(verbose_name=_('name'), max_length=120)
    last_name = models.CharField(verbose_name=_('surname'), max_length=120)
    bio = models.TextField(verbose_name=_('biography'), blank=True, null=True)

    def __str__(self):
      return f"{self.first_name} {self.last_name}"



class Article(models.Model):  
    author = models.ForeignKey(Reporter, max_length=150, verbose_name=_('author'), on_delete=models.PROTECT)
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
      return f'{self.author.first_name} - {self.headline}'
