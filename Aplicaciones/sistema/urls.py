from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    #Inicio URLS para las vistas de gestión de usuarios
    path('registrarUsuario/', views.registrarUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('editarUsuarios/<numDocumento>', views.edicionUsuarios),
    path('eliminarUsuarios/<numDocumento>', views.eliminarUsuario),
    #Fin URLS para las vistas de gestión de usuarios

    #Inicio URLS para las vistas de gestión de libros
    path('gestionLibros/', views.gestionLibros),
    path('registrarLibro/', views.registrarLibro),
    path('editarLibro/', views.editarLibro),
    path('gestionLibros/editarLibros/<ISBN>', views.edicionLibros),
    path('gestionLibros/eliminarLibros/<ISBN>', views.eliminarLibro),
    #Fin URLS para las vistas de gestión de libros

    #Inicio URLS para las vistas de gestión de prestamos
    path('gestionPrestamos/', views.gestionPrestamos),
    path('registrarPrestamo/', views.registrarPrestamo),
    path('editarPrestamo/', views.editarPrestamo),
    path('gestionPrestamos/editarPrestamos/<IDprestamo>', views.edicionPrestamos),
    path('gestionPrestamos/eliminarPrestamos/<IDprestamo>', views.eliminarPrestamo)
    #Fin URLS para las vistas de gestión de prestamos
]