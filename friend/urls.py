from django.conf.urls import url,include
from . import views
from .views import (
    FriendAPIView,
)


urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^$',  FriendAPIView.as_view() ),
]