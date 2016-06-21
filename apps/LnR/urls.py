from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index, name = "users"),
    url(r'^register$', views.register ),
    url(r'^login$', views.login ),
    url(r'^success$', views.success ),

]
