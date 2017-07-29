from django.conf.urls import url
from records.views import aadharentryview, login, profile
from . import views


urlpatterns = [
    url(r'^aadharentry/', aadharentryview, name='aadharentry'),
    url(r'^login/', login, name='Login'),
    url(r'^profile/', profile, name='profile'),
    url(r'^$', views.index)
]
