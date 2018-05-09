from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePage),
    url(r'^login/$', views.check_user_in_db),
    #student crud operations
url(r'^EditStudentSchool/(?P<id>\d+)/$', views.editSchool),
    url(r'^EditStudentCollage1/(?P<id>\d+)/$', views.editCollage1),
url(r'^EditStudentCollage2/(?P<id>\d+)/$', views.editCollage2),
url(r'^guideview/(?P<id>\d+)/(?P<id2>\d+)$', views.guideProfileView),
    url(r'^sponsoreview/(?P<id>\d+)/(?P<id2>\d+)$', views.sponsorProfileView),
url(r'^studentprofileview/(?P<id>\d+)/(?P<id2>\d+)$', views.StudentProfileView),
url(r'^studentprofileview2/(?P<id>\d+)/(?P<id2>\d+)$', views.StudentProfileView2),
url(r'^forgotpassword/$', views.forgotpass),
url(r'^backtoguide/(?P<id>\d+)$', views.BackToGuide),
url(r'^backtosponsor/(?P<id>\d+)$', views.BackToSponsor),
url(r'^backtostudent/(?P<id>\d+)$', views.BackToStudent),
url(r'^messageSendToStudentFromGuide/(?P<id>\d+)/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', views.messageSendToStudentFromGuide),
url(r'^messageSendToGuideFromStudent/(?P<id>\d+)/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', views.messageSendToGuideFromStudent),




url(r'^logout/$', views.logout_user),
]
