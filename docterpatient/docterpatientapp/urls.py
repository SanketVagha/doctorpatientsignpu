from django.contrib import admin
from django.urls import path
from docterpatientapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('checkemailExists', views.checkemailExists, name="checkemailExists"),
    path('checkuserExists', views.checkuserExists, name="checkuserExists"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login")
]


if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)