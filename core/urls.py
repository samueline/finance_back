"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import urls
from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from rest_framework import routers
from core.views.gastos import GastoViewSet

from core.views.ingresos import IngresosViewSet
from core.views.users import UserViewSet,GroupViewSet
from core.views.tareas import TareasViewSet




router = routers.DefaultRouter()

# router.register(r'users',UserViewSet)
router.register(r'group',GroupViewSet)
# router.register(r'ingreso',IngresosViewSet)
# router.register(r'ingreso',IngresosList.as_view())
router.register(r'gastos',GastoViewSet)
router.register(r'tareas',TareasViewSet)


urlpatterns = [
 path('',include(router.urls)),
#  path('ing/',include('core.ingress.urls')),
 path('admin/', admin.site.urls),
 path('ingreso/', IngresosViewSet.as_view({'get':'listar'})),

  path('ingreso/crear', IngresosViewSet.as_view({'post':'crear'})),
  path('ingreso/upt/<int:id>', IngresosViewSet.as_view({'put':'actualizar'})),
 path('total/', IngresosViewSet.as_view({'get':'porcentajes'})),
    

# gastos path
    
  path('gastos/list', GastoViewSet.as_view({'get':'listar'})),

  path('gastos/crear', GastoViewSet.as_view({'post':'crear'})),

  path('gastos/update/<int:id>', GastoViewSet.as_view({'put':'actualizar'})),

# tareas path
  path('tareas/listar', TareasViewSet.as_view({'get':'listar'})),

  path('tareas/crear/', TareasViewSet.as_view({'post':'crear'})),
  path('tareas/update/<pk>', TareasViewSet.as_view({'put':'actualizar'})),

  path('tareas/eliminar/<int:pk>', TareasViewSet.as_view({'delete':'eliminar'})),

  
#  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))   
 path('login/listar', UserViewSet.as_view({'get':'listar'})),

  path('login/', UserViewSet.as_view({'post':'login'})),
  path('signup/', UserViewSet.as_view({'post':'signup'})),

]
