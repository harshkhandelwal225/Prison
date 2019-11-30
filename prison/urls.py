"""prison URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
        path('admin/', admin.site.urls),
        path('register/',user_views.register,name='register'),
        path('',auth_views.LoginView.as_view(template_name='testapp/login.html'),name='login'),
        path('logout/',auth_views.LogoutView.as_view(template_name='testapp/logout.html'),name='logout'),
        path('home/',user_views.home,name='home'),
        path('fir/',user_views.fir,name='fir'),
        path('addprisoner/',user_views.addprisoner,name='addprisoner'),
        path('prisoner/<int:pk>',user_views.show,name="show"),
        path('addvisitor/',user_views.addvisitor,name='addvisitor'),
        path('addguard/',user_views.addguard,name='addguard'),
        path('crimegraph/',user_views.graphcrime,name='crimegraph'),
        path('crimeinput/',user_views.crimeinput,name='crimeinput'),
        path('displaypri/',user_views.displaypri,name='displaypri'),
        path('displayvis/',user_views.displayvis,name='displayvis'),
        path('capture/',user_views.capture,name='capture'),
        path('priupdate/<int:pk>',user_views.priupdate,name='prisoner-update')

]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
