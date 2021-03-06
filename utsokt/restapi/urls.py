from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^story/$', views.list_or_create),
    url(r'^story/(?P<story_id>\w+)$', views.modify_story),
    url(r'^story/(?P<story_id>\w+)/(?P<state>\w+)$', views.set_story_state),
]
