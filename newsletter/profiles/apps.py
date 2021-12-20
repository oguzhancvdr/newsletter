from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    # biz signal dosyamızda profiles'ı çoktan import ettik
    # yani signals.py yüklenmeden önce bu profillermin yüklenmesi lazım
    # bu profiller signals.py içindeki,
    # bundan dolayı bu app dosyası okunmaya hazır olduğunda
    # signal dosyamızı direk import etmesini istiyoruz

    def ready(self):
        import  profiles.signals
