from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_(
        'User'), on_delete=models.CASCADE)  # user.profile_set
    bio = models.CharField(max_length=255, blank=True,
                           null=True, verbose_name=_('Biography'))
    city = models.CharField(max_length=120, blank=True,
                            null=True, verbose_name=_('City'))
    avatar = models.ImageField(blank=True, null=True, verbose_name=_('Avatar'),
                               upload_to='profile_photos/%Y/%m/')

    def __str__(self) -> str:
        return self.user.username

    # burda Pillow kütüphanesi yardımı ile kullanıcının yüklemeye çalıştığı resimlerin
    # boyutlarını sınırlandık ve bir standart haline getirdik (600px, 600px)
    def save(self, *args, **kwargs):
        # Image Resize
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, verbose_name=_(
        'User Profile'), on_delete=models.CASCADE)
    status_message = models.CharField(
        max_length=255, verbose_name=_('Status Message'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created Date'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated Date'))

    class Meta:
        verbose_name_plural = _('Profile Statuses')

    def __str__(self) -> str:
        # user_profile bir profil nesnesidir foreign key ile bağlı olduğu için
        # biz burda str diğerek bir üst modelde tanımladığımız str methodunun
        # return ettiği değeri alıyoruz
        return str(self.user_profile)
