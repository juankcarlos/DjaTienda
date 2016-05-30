"""DjaTienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from  carrito import views as vc
urlpatterns = [


                  url(r'^$', vc.ver, name='home'),
                  url(r'^detalles/(?P<idprod>\d+)/detalles', vc.detalles, name='detalles'),
                  url(r'^comprobar', vc.checar, name='comprobar'),
                  url(r'^add/', vc.anadir, name='add'),
                  url(r'^formlog/', vc.logform, name='cargar'),
                  url(r'^registrar/', vc.form, name='registrar'),
                  url(r'^logout/', vc.salir, name='logout'),
                  url(r'^login/', vc.log, name='login'),
                  url(r'^foraddpre/', vc.addprod, name='foraddpre'),
                  url(r'^regprod/', vc.regprod, name="regprod"),
                  url(r'^carrocomp/', vc.vcarrito, name="carrocomp"),
                  url(r'^rm/(?P<idpr>\d+)/eliminarpr', vc.eliminardecarrito, name="rm"),
                  url(r'^vccat/(?P<nomcat>\w+)/verpr', vc.productoporcategoria, name="vccat"),
                  url(r'^fincompra/', vc.finalizar, name='fincompra'),
    #url(r'^e/(?P<vistaid>\d+)/', 'blog.views.vista'),  # formulario para editar
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

