from . import views
from django.urls import path, re_path

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="list"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail")
]