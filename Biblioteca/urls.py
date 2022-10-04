from django.contrib import admin
from django.urls import path
from BibliotecaApp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('<int:id>/',views.update_data, name='updatedata'),
    path('pag_user',views.pag_user, name='pag_user'),
    path('login/',auth_views.LoginView.as_view(template_name='Usuarios/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/',views.UsuarioCreate.as_view(), name='registrar'),
    path('alugar/<int:id>', views.alugar, name='alugar')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
