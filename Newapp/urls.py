from django.conf.urls import url
from . import views


app_name='Newapp'

urlpatterns=[
    url(r'ThanksForRegistering',views.thanks,name='thanksforregistering'),
    url(r'^export/$', views.download, name='download'),
    url(r'^Download/', views.extract, name='extract'),
]
