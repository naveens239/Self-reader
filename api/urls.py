from django.conf.urls import  url
from api import views

urlpatterns = [
      url(r'^passages/$', views.passage_list, name='passage_list'),
    url(r'^subjects/$', views.subject_list, name='subject_list'),


]