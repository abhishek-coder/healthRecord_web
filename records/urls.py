from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^patient-connect/$', views.patient_connect, name='patient_connect'),
    url(r'^doctor-login/$', views.doctor_login, name='doctor_login'),
    url(r'^patient-detail/(?P<patient_id>\d+)/', views.patient_detail,
        name='patient_detail'),
    url(r'^logout/$', logout, {'next_page': '/'})
]
