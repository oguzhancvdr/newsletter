from django.contrib.auth.models import User
from profiles.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver

# User modelimizde bir işlem gerçekleştiğinde;
# yani yeni bir user oluşturulup kaydedildiğinde
# post_save signal methodu benim aşağıda oluşturduğum create_profil functionumu
# tetiklesin bu signali aldıktan sonra
# burda biz sisteme bir kullanıcı dahil olduğunda otomatikmen onun
# Profilini oluşturuyoruz
@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    print(instance.username, '__Created: ', created)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_first_status_message(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(
            user_profile=instance,
            status_message=f'{instance.user.username} has been joined in the Ninja Club!'
        )

