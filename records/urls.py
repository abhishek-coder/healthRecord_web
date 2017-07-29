from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^patient-connect/$', views.patient_connect, name='patient_connect'),
    url(r'^doctor-login/$', views.doctor_login, name='doctor_login'),
    url(r'^patient-detail/(?P<patient_id>\d+)/$', views.patient_detail, name='patient_detail'),
    url(r'^patient-detail/(?P<patient_id>\d*)/history/$', views.history, name='history'),
    url(r'^patient-detail/(?P<patient_id>\d*)/history/(?P<case_id>\d*)/$',
        views.case_detail, name='case_detail'),
    url(r'^patient-detail/(?P<patient_id>\d+)/new-case/$', views.new_case, name='new_case'),
    url(r'^logout/$', logout, {'next_page': '/'}),

]
