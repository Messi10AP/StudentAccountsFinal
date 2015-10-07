from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static  
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='home'),
    url(r'^/register/$', views.signup, name='signup'),
    url(r'^/login/$', views.signin, name='signin'),
    url(r'^/signup/$', views.signup, name='signup'),
    url(r'^/info/$', views.studentinfo, name='studentinfo'),
]
#]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
