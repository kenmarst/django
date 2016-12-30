"""BR06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import user, group, face, recognition, connection

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api/user/add/?$', user.add),
    url(r'^api/user/update/?$', user.update),
    url(r'^api/user/delete/?$', user.delete),
    url(r'^api/user/list/?$', user.list),
]

urlpatterns += [
    url(r'^api/group/list/?$', group.list),
]

urlpatterns += [
    url(r'^api/face/add/?$', face.add),
    url(r'^api/face/delete/?$', face.delete),
    url(r'^api/face/list/?$', face.list),
]

urlpatterns += [
    url(r'^api/recognition/face/verify/?$', recognition.face_verify),
    url(r'^api/recognition/face/identify/?$', recognition.face_identify),
    url(r'^api/recognition/face/check/?$', recognition.face_check),
    url(r'^api/recognition/RFID/verify/?$', recognition.rfid_verify),
    url(r'^api/recognition/RFID/check/?$', recognition.rfid_check),
]

urlpatterns += [
    url(r'^api/connection/check/?$', connection.check),
    url(r'^api/connection/get/?$', connection.get),
    url(r'^api/connection/set/?$', connection.set),
]
