from django.http import request
from rest_framework import permissions
from pprint import pprint



class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsCommentOwnerOrReadOnly(permissions.BasePermission):
    # Bizim burda model'den türetilen neseneye(object)'e 
    # ulaşacak bir permission classı gerekiyor, Bunuda
    # içinde has_object_permission metodu bulunan BasePermission'a
    # ulaşarak kullanabiliriz
    # bu method 4 parametreye sahip
    # 1.self = bu classdan türeyecek olan nesne
    # 2.request = request objemiz bununla şuan ki kullanıcımıza ulaşabileceğiz
    # 3.view = biz bu permiisonu Comment ile alaklı view'de tanımlayacağımız için
    # view'ımize rahatlıkla ulaşabilcek
    # son obj ise ilgili modelden türeyen 'Comment' objesidir
    # ve biz bu obj sayesinde o obj içindeki yorum sahibine ulaşıp
    # şuan ki kullanıcyla aynı olup olmadığına bakıyoruz
    # ona göre boolean değer döndürüyoruz
    # böylelikle bir kullanıcı başka kullanıcının yorumunu ne update
    # ne delete , ne de post işlemi yapabilcek sadece read edebilcek
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner


# pprint(dir(IsAdminUserOrReadOnly))