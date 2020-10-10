from django.urls import path
from django.conf.urls import url
from .views import RegisterView, ActiveView, LoginView

app_name = 'user'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    # path(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    url(r"^active/(?P<token>.*)/$", ActiveView.as_view(), name='active'),
    path('login', LoginView.as_view(), name='login'),
]
