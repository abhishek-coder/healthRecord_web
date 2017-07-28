from django.conf.urls import url

from . import views


urlpatterns = [
    url('^login/$', views.LoginAPI.as_view()),
    url('^patient/cases/$', views.CaseListAPI.as_view()),
    url('^patient/case/$', views.CaseDetailAPI.as_view())
]
