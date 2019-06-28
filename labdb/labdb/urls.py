"""labdb URL Configuration

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
from django.urls import path, include
from labdb import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Vamk_Rs', views.Vamk_RViewSet)
router.register(r'Vamk_Cs', views.Vamk_CViewSet)
router.register(r'Vamk_R_Smds', views.Vamk_R_SmdViewSet)
router.register(r'VAMK_C_SMDs', views.VAMK_C_SMDViewSet)
router.register(r'Vamk_74HCXXs', views.Vamk_74HCXXViewSet)
router.register(r'Vamk_D', views.Vamk_DViewSet)
router.register(r'Vamk_Ana', views.Vamk_AnaViewSet)
router.register(r'Vamk_CPU', views.Vamk_CPUViewSet)
router.register(r'Vamk_CPU_SMD', views.Vamk_CPU_SMDViewSet)
router.register(r'Vamk_Con', views.Vamk_ConViewSet)
router.register(r'Vamk_IC_SMD', views.Vamk_IC_SMDViewSet)
router.register(r'Vamk_IC', views.Vamk_ICViewSet)
router.register(r'Vamk_Misc', views.Vamk_MiscViewSet)
router.register(r'Feeds', views.FeedViewSet)
router.register(r'Vamk_Socket', views.Vamk_SocketViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include (router.urls)),
    path('api-auth/', include ('rest_framework.urls', namespace='rest_framework')),
]
