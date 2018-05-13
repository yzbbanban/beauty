from django.contrib import admin
from django.conf.urls import url
import miao.views as mv

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', mv.index),
]
