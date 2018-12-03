from django.conf.urls import url
from .import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url('reset/<uuid:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]