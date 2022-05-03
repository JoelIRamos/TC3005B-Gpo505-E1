from django.urls import path
from api import views

urlpatterns = [
    # Rutas GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<int:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getLastSession/<int:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    
    # Rutas PUTs
    # * Actualizar los detalles del historial de un usuario
    path('putHistory/<int:userID>/', views.updateHistoryView.as_view(), name='put_last_session'),
    
    # Rutas POSTs
    # * Crear un nuevo historial
    path('postHistory/<int:userID>/', views.insertToHistoryView.as_view(), name='post_history'),
    # * Crear un nuevo registro de una sesion
    path('postLastSession/<int:userID>/<historyID>/', views.insertLastSessionView.as_view(), name='post_last_session'),
    
    # Rutas DELETEs
    # * Eliminar una sesion
    path('deleteLastSession/<int:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),

    # Rutas de la subida de archivos
    path('upload_file/', views.FileUploadView.as_view(), name='upload_file')
]